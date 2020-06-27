import cv2
from glob import glob
import numpy as np
import os 

link_img = glob('D:/DDSM_KhoaLuanTN/data_add_padding/Mass Train All JPEGs Full/*.jpg')
# print(len('LEFT_CcC_FULL.jpg'))
def add_padding(link_img):
    for i in link_img:
        img = cv2.imread(i)
        if('LEFT' in i[-25:]):
            img = cv2.copyMakeBorder(img, 0, 0, 1200, 0, cv2.BORDER_CONSTANT)
            cv2.imwrite(os.path.join('D:/DDSM_KhoaLuanTN/data_add_padding/Calc Train All Full JPEGs',i[-25:]), img)
        if( 'RIGHT' in i[-25:]):
            img = cv2.copyMakeBorder(img, 0, 0, 0, 1200, cv2.BORDER_CONSTANT)
            cv2.imwrite(os.path.join('D:/DDSM_KhoaLuanTN/data_add_padding/Calc Train All Full JPEGs',i[-25:]), img)
        
# add_padding(link_img)
def add_padding2(link_img):
    for i in link_img:
        img = cv2.imread(i)
        img = cv2.copyMakeBorder(img, 0, 0, 1000, 1000, cv2.BORDER_CONSTANT)
        cv2.imwrite(os.path.join('D:/DDSM_KhoaLuanTN/data_add_padding/Mass Train All JPEGs Full',i.split('\\')[-1]), img)
        print(i.split('\\')[-1])
add_padding2(link_img)
# print(len(link_img))