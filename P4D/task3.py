import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dirpath',
    type=str,
    default=os.getcwd()
)

args = parser.parse_args()

missing_list_file = os.path.join(args.dirpath, "missing.txt")

with open(missing_list_file, 'r', encoding='utf-8') as f:
    for file in f.readlines():
        filepath = os.path.join(args.dirpath, file.rstrip())
        with open(filepath, "w+") as f2:
            pass
