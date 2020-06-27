import os
from glob import glob
import pandas as pd 

link_img = glob(r'D:\DDSM_KhoaLuanTN\testpy\photo_box\New folder\*.JPG')
link_copy = r'D:\DDSM_KhoaLuanTN\testpy\photo_box\New folder\_cala_train'

for i in link_img:
    stri = os.path.join(link_copy, i.split('\\')[-1].split(".")[-2] + '.jpg')
    print(stri)
    os.rename(i, stri)
