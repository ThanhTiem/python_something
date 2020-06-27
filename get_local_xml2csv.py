import cv2
from glob import glob
import os
import re 
import pandas as pd 


filetxt = r'D:\DDSM_KhoaLuanTN\testpy\new_label.txt'
with open(filetxt, 'r', encoding='utf8') as f:
    text = f.readlines()
    # print(text)
    for i in text:
        a = i.split(',')
        # print(a,"\n----")
        x = a[1]
        y = a[2]
        w = a[3]
        h = a[4]
        link_img = a[0]
        img  = cv2.imread(link_img)
        print("aaaa: ", x, "-", y,"-", w, "-", h)
        im = cv2.rectangle(img, (int(x), int(y)), (int(w), int(h)), (0, 0, 255), 2)
        cv2.imwrite(os.path.join('D:/DDSM_KhoaLuanTN/testpy/photo_box', link_img[-25:]), im)
