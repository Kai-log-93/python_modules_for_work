# 导入所需的模块
import os
import cv2

# 定义源文件夹和目标文件夹的路径
source_folder = "E:/books/cover/origin"
target_folder = "E:/books/cover"

# 定义目标图片的高度和宽度
target_height = 1042
target_width = 768

# 遍历源文件夹中的所有图片文件
for file in os.listdir(source_folder):
    # 获取图片文件的完整路径
    file_path = os.path.join(source_folder, file)
    # 读取图片文件
    image = cv2.imread(file_path)
    # 获取图片的高度和宽度
    height, width = image.shape[:2]
    # 计算图片的高宽比
    aspect_ratio = height / width
    # 判断图片的高宽比是否大于目标图片的高宽比
    if aspect_ratio > target_height / target_width:
        # 如果是，那么先将图片的宽度缩放到目标宽度，保持长宽比不变
        scale = target_width / width
        resized_image = cv2.resize(image, (target_width, int(height * scale)))
        # 然后计算裁切区域的左上角和右下角坐标，使得裁切后的图片为1024*768，且居中
        x1 = 0
        y1 = (resized_image.shape[0] - target_height) // 2
        x2 = target_width
        y2 = y1 + target_height
        # 使用坐标对图片进行裁切
        cropped_image = resized_image[y1:y2, x1:x2]
    else:
        # 如果不是，那么先将图片的高度缩放到目标高度，保持长宽比不变
        scale = target_height / height
        resized_image = cv2.resize(image, (int(width * scale), target_height))
        # 然后计算裁切区域的左上角和右下角坐标，使得裁切后的图片为1024*768，且居中
        x1 = (resized_image.shape[1] - target_width) // 2
        y1 = 0
        x2 = x1 + target_width
        y2 = target_height
        # 使用坐标对图片进行裁切
        cropped_image = resized_image[y1:y2, x1:x2]
    # 获取目标文件夹中的图片文件名，添加后缀"_cropped"以区分原始图片
    target_file = file[:-4] + "_cropped" + file[-4:]
    # 获取目标文件夹中的图片文件的完整路径
    target_path = os.path.join(target_folder, target_file)
    # 将裁切后的图片保存到目标文件夹中
    cv2.imwrite(target_path, cropped_image)
