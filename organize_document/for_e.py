# 导入所需的模块
import os
import shutil
from PIL import Image, ExifTags
import time
import random
import random
import string
from PIL import Image
from PIL.ExifTags import TAGS

# 定义源文件夹和目标文件夹
source_folder = "E:/MyFurStuffs" # 你的E盘
target_folder = "E:/Media" # 你想要存放整理后的文件的文件夹

# 定义生成随机字符串的函数
def random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

# 如果目标文件夹不存在，就创建一个
if not os.path.exists(target_folder):
    os.mkdir(target_folder)


# 遍历源文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(source_folder):
    # 对于每一个文件，判断是否是图片或视频
    for file in files:
        # 获取文件的绝对路径
        file_path = os.path.join(root, file)
        # 获取文件的扩展名
        file_ext = os.path.splitext(file)[1].lower()
        # 定义图片和视频的扩展名列表
        image_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        video_exts = [".mp4", ".avi", ".mov", ".wmv", ".flv"]
        # 如果文件是图片或视频，就进行处理
        if file_ext in image_exts or file_ext in video_exts:
            # 根据文件类型创建子文件夹
            if file_ext in image_exts:
                sub_folder = "Images"
            else:
                sub_folder = "Videos"
            # 获取子文件夹的绝对路径
            sub_folder_path = os.path.join(target_folder, sub_folder)
            # 如果子文件夹不存在，就创建一个
            if not os.path.exists(sub_folder_path):
                os.mkdir(sub_folder_path)
            # 获取文件的修改时间，并转换为日期格式
            file_mtime = os.path.getmtime(file_path)
            file_date = time.strftime("%Y%m%d", time.localtime(file_mtime))
            # 获取文件的像素分辨率
            if file_ext in image_exts:
                # 使用 PIL 模块获取图片的宽度和高度
                image = Image.open(file_path)
                width, height = image.size
                # 如果图片有 EXIF 信息，就尝试获取拍摄日期
                try:
                    exif = image._getexif()
                    if exif:
                        for tag, value in exif.items():
                            decoded = ExifTags.TAGS.get(tag, tag)
                            if decoded == "DateTimeOriginal":
                                file_date = value.replace(":", "")[:8]
                except:
                    pass
            else:
                # 使用 ffprobe 命令获取视频的宽度和高度（需要安装 ffmpeg）
                cmd = f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 {file_path}"
                output = os.popen(cmd).read().strip()
                width, height = output.split(",")
            # 定义像素分辨率的格式
            file_resolution = f"{width}x{height}"
            # 定义文件随机名
            rand_str = random_string(8)
            # 定义新的文件名，包括日期，类型缩写，像素分辨率和原始扩展名
            new_file_name = f"{file_date}_{sub_folder[0]}_{file_resolution}_{rand_str}{file_ext}"
            # 获取新文件的绝对路径
            new_file_path = os.path.join(sub_folder_path, new_file_name)
            # 复制原始文件到新文件夹，并重命名为新的文件名
            shutil.copy(file_path, new_file_path)
