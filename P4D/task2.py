import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dirpath',
    type=str,
    default=os.getcwd()
)
parser.add_argument(
    '--files',
    type=str,
    nargs='+',
    required=True
)

args = parser.parse_args()

existing = []
missing = []

for filename in args.files:
    file_path = os.path.join(args.dirpath, filename)
    if os.path.isfile(file_path):
        existing.append(filename)
    else:
        missing.append(filename)

existing_list_file = os.path.join(args.dirpath, "existing.txt")
missing_list_file = os.path.join(args.dirpath, "missing.txt")

with open(existing_list_file, 'w', encoding='utf-8') as f:
    print("Список файлов, присутствующих в папке:")
    for file in existing:
        f.write(file + "\n")
        print(file)

with open(missing_list_file, 'w', encoding='utf-8') as f:
    print("Список файлов, отсутствующих в папке:")
    for file in missing:
        f.write(file + "\n")
        print(file)
