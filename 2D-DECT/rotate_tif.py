from PIL import Image
import os
from tqdm import tqdm


# 读取路径下图片的名称
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            img_name = os.path.split(file)[1]
            L.append(img_name)
    return L


# file_dir = "out/"
# for root, dirs, files in os.walk(file_dir):
#     for dir in dirs:
#         os.mkdir(file_dir + 'rotate_' + dir)

dirname = 'BIMCV_2/'
file_dir = "out/" + dirname
filenames = file_name(file_dir)
if not os.path.exists('Images/original_data/' + dirname):
    os.mkdir('Images/original_data/' + dirname)
for filename in tqdm(filenames):
    src_img = Image.open(file_dir + filename)
    src_roi = src_img.rotate(90)
    # src_roi.show()
    src_roi.save('Images/original_data/' + dirname + filename)

