# 导入必要的模块
import os
import shutil
import random
import string
from PIL import Image
from PIL.ExifTags import TAGS
import time

# 定义目标文件夹的路径
TARGET_FOLDER = "E:\\Media"

# 定义图片和视频文件的扩展名列表
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mov", ".wmv", ".flv"]

# 定义生成随机字符串的函数
def random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

# 定义格式化日期的函数
def format_date(date):
    return date.replace(":", "-").split()[0]

# 遍历E盘里的所有文件
for root, dirs, files in os.walk("E:\\MyFurStuffs"):
    for file in files:
        # 获取文件的绝对路径和扩展名
        file_path = os.path.join(root, file)
        file_ext = os.path.splitext(file)[1].lower()
        # 判断是否是图片或视频文件
        if file_ext in IMAGE_EXTENSIONS or file_ext in VIDEO_EXTENSIONS:
            # 复制文件到目标文件夹中
            shutil.copy(file_path, TARGET_FOLDER)
            # 获取复制后文件的绝对路径和名称
            new_file_path = os.path.join(TARGET_FOLDER, file)
            new_file_name = os.path.basename(new_file_path)
            # 根据文件类型创建子文件夹
            if file_ext in IMAGE_EXTENSIONS:
                sub_folder = "Images"
            else:
                sub_folder = "Videos"
            sub_folder_path = os.path.join(TARGET_FOLDER, sub_folder)
            if not os.path.exists(sub_folder_path):
                os.mkdir(sub_folder_path)
            # 将文件移动到相应的子文件夹中
            shutil.move(new_file_path, sub_folder_path)
            # 获取移动后文件的绝对路径和名称
            final_file_path = os.path.join(sub_folder_path, new_file_name)
            final_file_name = os.path.basename(final_file_path)
            # 根据日期标签、像素和随机字符串重新命名文件
            if file_ext in IMAGE_EXTENSIONS:
                # 读取图片元数据
                image = Image.open(final_file_path)
                exif_data = image.getexif()
                # 获取图片日期标签
                date_tag = exif_data.get(36867) # 36867 is the tag id for DateTimeOriginal
                if date_tag:
                    date = format_date(date_tag)
                else:
                    # 如果没有日期标签，则使用文件创建时间代替
                    date = format_date(time.ctime(os.path.getctime(final_file_path)))
                # 获取图片像素
                width, height = image.size
                pixel = f"{width}x{height}"
                # 生成随机字符串
                rand_str = random_string(8)
                # 按照规则组合新的文件名称
                new_file_name = f"{date}_{pixel}_{rand_str}{file_ext}"
            else:
                # 获取视频文件创建时间
                date = format_date(time.ctime(os.path.getctime(final_file_path)))
                # 生成随机字符串
                rand_str = random_string(8)
                # 按照规则组合新的文件名称
                new_file_name = f"{date}_{rand_str}{file_ext}"
            # 重命名文件
            os.rename(final_file_path, os.path.join(sub_folder_path, new_file_name))
