import cv2
import numpy as np 
import re 
import os
from glob import glob


link_txt = glob(r'D:\DDSM_KhoaLuanTN\darknet\data\label_0\*.txt')
b = []
for file in link_txt:
    with open(file, 'r', encoding='utf8') as f:
        leng = f.read()
        # if(len(leng) == 113):
        #     b.append(file)
        #     print(file)
    print(len(leng))    
# print(len(b))