# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Fine-tuning the library models for language modeling on a text file (GPT, GPT-2, BERT, RoBERTa).
GPT and GPT-2 are fine-tuned using a causal language modeling (CLM) loss while BERT and RoBERTa are fine-tuned
using a masked language modeling (MLM) loss.
"""

from __future__ import absolute_import, division, print_function
import pandas as pd
import argparse
import glob
import logging
import os

import random
import numpy as np
import torch
import multiprocessing
from tqdm import tqdm


from torch.utils.data import DataLoader, Dataset, SequentialSampler, RandomSampler, TensorDataset
from torch.utils.data.distributed import DistributedSampler
from transformers import (WEIGHTS_NAME, AdamW, get_linear_schedule_with_warmup,
                          RobertaConfig, RobertaModel, RobertaTokenizer)

from model import Model

logger = logging.getLogger(__name__)
cpu_cont = 16


def get_example(item):
    tokenizer, code1, code2, block_size = item
    try:
        code_1 = ' '.join(code1.split())
    except:
        code_1 = ""
    code1 = tokenizer.tokenize(code_1)


    try:
        code_2 = ' '.join(code2.split())
    except:
        code_2 = ""
    code2 = tokenizer.tokenize(code_2)


    return convert_examples_to_features(code1, code2, tokenizer, block_size)


class InputFeatures(object):
    """A single training/test features for a example."""

    def __init__(self,
                 input_tokens,
                 input_ids,
                 ):
        self.input_tokens = input_tokens
        self.input_ids = input_ids



def convert_examples_to_features(code1_tokens, code2_tokens,tokenizer, block_size):
    """convert examples to token ids"""
    code1_tokens = code1_tokens[:block_size - 4]
    code1_tokens = [tokenizer.cls_token, "<encoder-only>", tokenizer.sep_token] + code1_tokens + [tokenizer.sep_token]
    code2_tokens = code2_tokens[:block_size - 4]
    code2_tokens = [tokenizer.cls_token, "<encoder-only>", tokenizer.sep_token] + code2_tokens + [tokenizer.sep_token]

    code1_ids = tokenizer.convert_tokens_to_ids(code1_tokens)
    padding_length = block_size - len(code1_ids)
    code1_ids += [tokenizer.pad_token_id] * padding_length

    code2_ids = tokenizer.convert_tokens_to_ids(code2_tokens)
    padding_length = block_size - len(code2_ids)
    code2_ids += [tokenizer.pad_token_id] * padding_length

    source_tokens = code1_tokens + code2_tokens
    source_ids = code1_ids + code2_ids
    return InputFeatures(source_tokens, source_ids)


class TextDataset(Dataset):
    def __init__(self, tokenizer, csv_file, block_size,pool=None):
        self.examples = []

        data = []
        for index, row in csv_file.iterrows():
            data.append((tokenizer,  row['code1'],row['code2'],block_size))

        print('--- Data Loading ---')
        self.examples = pool.map(get_example, tqdm(data, total=len(data)))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, item):
        return torch.tensor(self.examples[item].input_ids)


def set_seed(seed=42):
    random.seed(seed)
    os.environ['PYHTONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True


def batch_predict(args, model, tokenizer, csv_file, pool):
    """ Evaluate the model """

    eval_dataset = TextDataset(tokenizer, csv_file, args.block_size, pool)

    eval_sampler = SequentialSampler(eval_dataset)
    eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args.batch_size, num_workers=0)

    model.eval()
    logits = []
    print('--- Model Running ---')
    for batch in tqdm(eval_dataloader):
        try:
            inputs = batch.to(args.device)
            with torch.no_grad():
                cos_sim = model(inputs, None)
                logits.append(cos_sim.cpu().numpy())
        except:
            logits.append(np.array([-1]))
    logits = np.concatenate(logits, 0)

    # print(logits)
    y_preds = logits > 0.5
    # debug
    # return logits
    return y_preds


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # parser.add_argument("--func_csv", default=None, type=str,
    #                     help="An optional input test data file to evaluate the perplexity on (a jsonl file).")
    # parser.add_argument("--model_path", default=None, type=str,
    #                     help="The model checkpoint for weights initialization.")
    # parser.add_argument("--local_model", default=None, type=str,
    #                     help="The saved trained model.")
    parser.add_argument("--block_size", default=512, type=int,
                        help="Optional input sequence length after tokenization.")
    parser.add_argument("--batch_size", default=4, type=int,
                        help="Batch size per GPU/CPU for evaluation.")
    parser.add_argument('--seed', type=int, default=42,
                        help="random seed for initialization")
    args = parser.parse_args()

    set_seed(args.seed)

    # set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    args.n_gpu = torch.cuda.device_count()
    args.device = device
    model_path = 'microsoft/unixcoder-base'
    tokenizer = RobertaTokenizer.from_pretrained(model_path)
    config = RobertaConfig.from_pretrained(model_path)
    model = RobertaModel.from_pretrained(model_path)

    model = Model(model, config, tokenizer, args)

    model.to(device)
    if args.n_gpu > 1:
        model = torch.nn.DataParallel(model)

    model_to_load = model
    model_to_load = model.module if hasattr(model, 'module') else model
    model_to_load.load_state_dict(torch.load('./saved_models/checkpoint-best-f1/model.bin'))

    pool = multiprocessing.Pool(cpu_cont)
    for folder in os.listdir('./Type-4 csv origin/'):
        print(folder)
        for file in os.listdir(os.path.join('./Type-4 csv origin/',folder)):
            target_csv = os.path.join('./Type-4 csv/',folder,file)
            if '.csv' not in file or os.path.exists(target_csv):
                continue
            func_csv = pd.read_csv(os.path.join('./Type-4 csv origin/',folder,file), encoding='utf-8')
    
            result = batch_predict(args, model, tokenizer, func_csv, pool=pool)

            pre_series = pd.Series(result)
            func_csv.insert(3,'predictions',pre_series)
            try:
                os.makedirs(os.path.join('./Type-4 csv/',folder))
            except:
                pass
            func_csv.to_csv(target_csv,index=None)

