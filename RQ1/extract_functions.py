import os
import json
import random
import re

def format_code_segment(function_code):
    ret_chars = re.sub(' |\n|\t', '', function_code.lower())

    return ret_chars

def filter_code(raw_code, comment):
    # Single_line
    raw_code_strip = raw_code[1:len(raw_code) - 1].strip()
    if raw_code_strip.count("\n") <= 0:
        # print(raw_code)
        return 1

    comment = format_code_segment(comment)

    # Duplicate Code
    if not content_list.__contains__(comment):
        content_list.append(comment)
    else:
        #print("Dup!!")
        return 1

    char_list = []
    # Less than 5 unique char
    char_count = 0
    for c in comment.strip():
        if c in builtins_char_list:
            continue
        else:
            if c not in char_list:
                char_list.append(c)
                char_count += 1
            else:
                continue

    if char_count <= 5:
        # print("LESS!!")
        return 1

    return 0

if __name__ == "__main__":
    star_idxs = [2048,4096]
    lang = "java"

    builtins_char_list = ['/', '*', ' ', '\n', '#']

    if lang == 'java' or lang == 'c':
        for i in range(len(star_idxs) - 1):
            pre_experiment_list = []
            left = star_idxs[i]
            right = star_idxs[i + 1]
            output_folder = 'StarsRange/cw/%s/%d_%d/' % (lang, left, right)
            fun_json = "func/%s/%s_func_star_%d_%d.json" % (lang, lang, left, right - 1)

            source_code_folder = output_folder + 'source/'
            prompt_folder = output_folder + 'prompt/' 

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            if not os.path.exists(source_code_folder):
                os.makedirs(source_code_folder)
            if not os.path.exists(prompt_folder):
                os.makedirs(prompt_folder)

            with open(fun_json, 'r', encoding='utf-8', errors='ignore') as f:
                content_list = []

                for (i, line) in enumerate(f):
                    l = json.loads(line)
                    # print(dict.keys())
                    raw_comment = l['docstring']
                    raw_code = l['code']
                    fun_head = l['func_signal']

                    processed_code = raw_comment + fun_head + raw_code

                    flag = filter_code(raw_code, raw_comment)

                    if not flag:
                        pre_experiment_list.append([i,l])

                # If you want to reproduce our pre-experiment, you can use this code.
                # Or you will get the full-data output.
                # pre_experiment_list = random.sample(pre_experiment_list, 100)

                for cur_line in pre_experiment_list:
                    i = cur_line[0]
                    info = cur_line[1]

                    comment = info['docstring']
                    code = info['code']
                    fun_head = info['func_signal']

                    source_code_segment = comment + fun_head + code

                    source_code_path = source_code_folder + '%05d' % (i) + '.%s' % lang
                    source_code = open(source_code_path, 'w', encoding='utf-8', errors='ignore')
                    source_code.write(source_code_segment)

                    test_folder = prompt_folder + 'test_%05d' % (i) + '/'
                    if not os.path.exists(test_folder):
                        os.mkdir(test_folder)

                    prompt_path = test_folder + 'prompt_%05d' % (i) + '.%s' % lang
                    prompt_file = open(prompt_path, 'w', encoding='utf-8', errors='ignore')


                    prompt = comment + fun_head + " \n{"
                    prompt_file.write(prompt)

    if lang == 'python':
        for i in range(len(star_idxs) - 1):
            pre_experiment_list = []
            left = star_idxs[i]
            right = star_idxs[i + 1]

            output_folder = 'StarsRange/gpt4o/python/%d_%d/' % (left, right)
            fun_json = "func/python/python_func_star_%d_%d.json" % (left, right - 1)

            source_code_folder = output_folder + 'source/'
            prompt_folder = output_folder + 'prompt/' 

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            if not os.path.exists(source_code_folder):
                os.makedirs(source_code_folder)
            if not os.path.exists(prompt_folder):
                os.makedirs(prompt_folder)

            with open(fun_json, 'r', encoding='utf-8', errors='ignore') as f:
                content_list = []

                for (i, line) in enumerate(f):
                    cur_line = json.loads(line)

                    raw_comment = cur_line['docstring'].replace('\n', '\n    ')
                    raw_code = cur_line['code'].replace('\n', '\n    ')
                    fun_head = cur_line['func_signal'].replace('\n', '\n    ')

                    processed_code = fun_head + raw_comment + raw_code
                    flag = filter_code(raw_code, raw_comment)

                    if not flag:
                        pre_experiment_list.append([i,cur_line])

                # pre_experiment_list = random.sample(pre_experiment_list, 100)

                for cur_line in pre_experiment_list:
                    i = cur_line[0]
                    info = cur_line[1]

                    raw_comment = info['docstring'].replace('\n', '\n    ')
                    raw_code = info['code'].replace('\n', '\n    ')
                    fun_head = info['func_signal'].replace('\n', '\n    ')

                    processed_code = fun_head + raw_comment + raw_code

                    source_code_path = source_code_folder + '%05d' % (i) + '.py'
                    source_code = open(source_code_path, 'w', encoding='utf-8', errors='ignore')
                    source_code.write(processed_code)
                    
                    test_folder = prompt_folder + 'test_%05d' % (i) + '/'
                    if not os.path.exists(test_folder):
                        os.mkdir(test_folder)

                    prompt_path = test_folder + 'prompt_%05d' % (i) + '.py'
                    prompt_file = open(prompt_path, 'w', encoding='utf-8', errors='ignore')


                    prompt = fun_head + raw_comment
                    prompt_file.write(prompt[:len(prompt) - 4])