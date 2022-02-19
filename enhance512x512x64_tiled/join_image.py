import torch
import numpy as np
from PIL import Image
import os
from skimage import io, transform
from skimage import img_as_float


def join_images(reconstructed_images):
    #reconstructed_images = "./."
    
    scan_list = os.listdir(reconstructed_images)
    #print(scan_list)
    print("Joining images in folder :", reconstructed_images)
    
    tile1_list = []
    tile2_list = []
    tile3_list = []
    tile4_list = []
    scan_name_list = []
    
    for scan in scan_list:
        if("tile1" in scan):
            tile1_list.append(scan)
            tile2_list.append(scan.replace("tile1", "tile3"))
            tile3_list.append(scan.replace("tile1", "tile2"))
            tile4_list.append(scan.replace("tile1", "tile4"))
            scan_name_list.append(scan.replace("tile1_", ""))

    #print(scan_name_list)
    
    for i in range(len(tile1_list)):
    
        folder1 = reconstructed_images + "/" + tile1_list[i]
        folder2 = reconstructed_images + "/" + tile2_list[i]
        folder3 = reconstructed_images + "/" + tile3_list[i]
        folder4 = reconstructed_images + "/" + tile4_list[i]
        
        img_list = os.listdir(folder1)
        
        img_list.sort()
        
        out_folder = reconstructed_images + "/" + scan_name_list[i]
        
        if not os.path.exists(out_folder):
                os.makedirs(out_folder)
        
        for img in img_list:
            img1 = io.imread(folder1 + "/" + img)
            img2 = io.imread(folder2 + "/" + img)
            img3 = io.imread(folder3 + "/" + img)
            img4 = io.imread(folder4 + "/" + img)
        
            out = np.zeros((512, 512))
            out[0:256, 0:256] = img1[0:256, 0:256]
            out[256:, 0:256] = img2[16:256+16, 0:256]
            out[0:256, 256:] = img3[0:256, 16:256+16]
            out[256:, 256:] = img4[16:256+16, 16:256+16]
    
            im_out = Image.fromarray(out)
            im_out.save(out_folder + "/" + img)


join_images("./visualize/test/mapped/input/")
join_images("./visualize/test/mapped/output/")
join_images("./visualize/test/mapped/target/")
join_images("./reconstructed_images/test/")

