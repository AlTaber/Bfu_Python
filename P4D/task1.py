import sys
import os
import shutil

try:
    path = sys.argv[1]
except:
    path = "P4D"

small_list = []
for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if not os.path.isfile(file_path): continue
    if os.path.getsize(file_path) < 2048:
        small_list.append(file_path)

small_path = os.path.join(path, "small")
os.makedirs(small_path, exist_ok=True)

for filepath in small_list:
    shutil.copy(filepath, small_path)
    