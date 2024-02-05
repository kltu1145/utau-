import os
import re
import time
from collections import Counter

current_folder = os.path.dirname(os.path.abspath(__file__))
exclude_file = os.path.basename(__file__)
name = []


def get_trailing_number(text):
    match = re.search(r'\d+$', text)
    if match:
        return match.group()
    return ''


def remove_trailing_digits(text):
    return re.sub(r'\d+$', '', text)


while True:
    name = []
    for filename in os.listdir(current_folder):
        namenum, ext = os.path.splitext(filename)
        filename1 = remove_trailing_digits(namenum)
        name.append(filename1)
        namesame = Counter(name)
        name1 = list(set(name))

    for filename in os.listdir(current_folder):
        if filename == exclude_file:
            continue

        name, ext = os.path.splitext(filename)
        num = re.search(r'\d+$', name)
        if num:
            num = int(num.group())

        elif name in name1:
            number = namesame[name]
            new_name = f'{name}{number}{ext}'
            print(f'重命名文件:{filename} -> {new_name}')
            src = os.path.join(current_folder, filename)
            dest = os.path.join(current_folder, new_name)
            os.rename(src, dest)

    time.sleep(1)
