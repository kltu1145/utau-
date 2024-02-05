import os

# 定义要添加的后缀
suffix = input("输入扩展名")

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 遍历当前目录下所有文件
for filename in os.listdir(current_dir):
    # 检查是否为文件，并排除自身
    if os.path.isfile(os.path.join(current_dir, filename)) and filename != os.path.basename(__file__) and filename != "addnumber.py" and filename != "jian1.py":
        # 提取原文件扩展名
        old_base_name, old_extension = os.path.splitext(filename)
        # 构建新文件名
        new_filename = suffix + old_base_name + old_extension
        # 生成旧文件和新文件的完整路径
        old_filepath = os.path.join(current_dir, filename)
        new_filepath = os.path.join(current_dir, new_filename)
        # 重命名文件
        os.rename(old_filepath, new_filepath)
        print(f"File '{filename}' has been renamed to '{new_filename}'")

print("Finished renaming files.")
