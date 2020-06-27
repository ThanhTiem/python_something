import os
import pandas as pd
import re
from glob import glob

link = r'C:\Users\ThanhTiem\Desktop\testpy\train.txt'
links = r'C:\Users\ThanhTiem\Desktop\testpy\trains.txt'
# os.rename(link, links)

txt = glob(r'D:\DDSM_KhoaLuanTN\CBIS-DDSM1\CBIS-DDSM\New folder\New folder\labels\*.txt')
print(len(txt))
arr = []
for im_name in txt:
    # a = im_name.replace("_MASK", "_FULL")
    a = im_name.replace("_1", "")
    # os.rename(im_name, a)
    # print(a)
    os.rename(im_name, a)
    arr.append(a)
print(len(arr))
# for i in txt:
#     for j in arr:
#         os.rename(i, j)
