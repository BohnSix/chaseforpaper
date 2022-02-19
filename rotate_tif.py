from PIL import Image, ImageFilter, ImageDraw, ImageEnhance
import random
import os
import numpy as np
from tqdm import tqdm

# 要裁剪图像的大小
img_w = 256
img_h = 256


# 读取路径下图片的名称
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            img_name = os.path.split(file)[1]
            L.append(img_name)

    return L


image_sets = file_name('./data/src')  # 图片存贮路径


# 添加噪声
def add_noise(img):
    drawObject = ImageDraw.Draw(img)
    for i in range(250):  # 添加点噪声
        temp_x = np.random.randint(0, img.size[0])
        temp_y = np.random.randint(0, img.size[1])
        drawObject.point((temp_x, temp_y), fill="white")  # 添加白色噪声点,噪声点颜色可变
    return img


# 色调增强
def random_color(img):
    img = ImageEnhance.Color(img)
    img = img.enhance(2)
    return img


def data_augment(src_roi, label_roi):
    # 图像和标签同时进行90，180，270旋转
    if np.random.random() < 0.25:
        src_roi = src_roi.rotate(90)
        label_roi = label_roi.rotate(90)
    if np.random.random() < 0.25:
        src_roi = src_roi.rotate(180)
        label_roi = label_roi.rotate(180)
    if np.random.random() < 0.25:
        src_roi = src_roi.rotate(270)
        label_roi = label_roi.rotate(270)
    # 图像和标签同时进行竖直旋转
    if np.random.random() < 0.25:
        src_roi = src_roi.transpose(Image.FLIP_LEFT_RIGHT)
        label_roi = label_roi.transpose(Image.FLIP_LEFT_RIGHT)
    # 图像和标签同时进行水平旋转
    if np.random.random() < 0.25:
        src_roi = src_roi.transpose(Image.FLIP_TOP_BOTTOM)
        label_roi = label_roi.transpose(Image.FLIP_TOP_BOTTOM)
    # 图像进行高斯模糊
    if np.random.random() < 0.25:
        src_roi = src_roi.filter(ImageFilter.GaussianBlur)
    # 图像进行色调增强
    if np.random.random() < 0.25:
        src_roi = random_color(src_roi)
    # 图像加入噪声
    if np.random.random() < 0.2:
        src_roi = add_noise(src_roi)
    return src_roi, label_roi


# image_num：增广之后的图片数据
def creat_dataset(image_num=100000, mode='original'):
    print('creating dataset...')
    image_each = image_num / len(image_sets)
    g_count = 0
    for i in tqdm(range(len(image_sets))):
        count = 0
        src_img = Image.open('./data/src/' + image_sets[i])  # 3 channels
        label_img = Image.open('./data/label/' + image_sets[i])  # 3 channels
        # 对图像进行随机裁剪，这里大小为256*256
        while count < image_each:
            width1 = random.randint(0, src_img.size[0] - img_w)
            height1 = random.randint(0, src_img.size[1] - img_h)
            width2 = width1 + img_w
            height2 = height1 + img_h

            src_roi = src_img.crop((width1, height1, width2, height2))
            label_roi = label_img.crop((width1, height1, width2, height2))

            if mode == 'augment':
                src_roi, label_roi = data_augment(src_roi, label_roi)
            src_roi.save('./data/train_src/%d.tif' % g_count)
            label_roi.save('./data/train_label/%d.tif' % g_count)
            count += 1
            g_count += 1


if __name__ == '__main__':
    # creat_dataset(mode='augment')
    src_img = Image.open('./data/src/' + image_sets[i])

