import argparse
import pandas as pd
from pathlib import Path
from clone_classifier import CloneClassifier


ROOT = Path(__file__).parent


def main():
    """Run the clone classifier on specified input file.

    By default, the input file is the C4 dataset located in `examples/c4.csv`,
    and its predictions output is saved as `results/res.csv`.

    Args:
        max_token_size: the maximum token size for the input data (default: 512)
        fp16: a flag to enable half-precision (default: False)
        input: the path to the input CSV file (default: 'examples/c4.csv')
        output: the path to save the output CSV file (default: 'results/res.csv')
        per_device_eval_batch_size: the batch size for evaluation per device (default: 32)
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--max_token_size", type=int, metavar="", default=512, help="Max token size"
    )
    parser.add_argument("--fp16", action="store_true", help="Enable half-precision")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        metavar="",
        default=f"{ROOT / 'examples/c4.csv'}",
        help="Input file path",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        metavar="",
        default=f"{ROOT / 'results/res.csv'}",
        help="Output file path",
    )
    parser.add_argument(
        "--per_device_eval_batch_size",
        type=int,
        metavar="",
        default= 2,
        help="Batch size per device for evaluation",
    )

    classifier_args = vars(parser.parse_args())
    input_path = 'Type-4 csv origin/python/16_32.csv'
    output_path = 'Type-4 csv/python/16_32.csv'

    clone_classifier = CloneClassifier(**classifier_args)

    df = pd.read_csv(input_path)
    results = pd.DataFrame(columns=list(['code1','code2','predictions']))
    for row_id in range(df.shape[0]):
        cur_result = clone_classifier.predict(df[row_id])
        results = pd.concats(results,cur_result)
    results.to_csv('tem.csv',encoding='utf-8')

    return


if __name__ == "__main__":
    main()
