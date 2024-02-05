import os
import re

current_folder = os.path.dirname(os.path.abspath(__file__))
exclude_file = os.path.basename(__file__)


def remove_trailing_digits(text):
    return re.sub(r'\d+$', '', text)


def get_trailing_number(text):
    match = re.search(r'\d+$', text)
    if match:
        return match.group()
    return 0


for filename in os.listdir(current_folder):
    if filename == exclude_file:
        continue
    name, ext = os.path.splitext(filename)
    num = int(get_trailing_number(name))
    if num - 1 == 0:
        new_name = f'{remove_trailing_digits(name)}{ext}'
        print(f'重命名文件:{filename} -> {new_name}')
        src = os.path.join(current_folder, filename)
        dest = os.path.join(current_folder, new_name)
        os.rename(src, dest)
    elif get_trailing_number(name) != 0:
        new_name = f'{remove_trailing_digits(name)}{str(num - 1)}{ext}'
        print(f'重命名文件:{filename} -> {new_name}')
        src = os.path.join(current_folder, filename)
        dest = os.path.join(current_folder, new_name)
        os.rename(src, dest)
