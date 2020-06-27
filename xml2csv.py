import numpy as np 
import pandas as pd 
import os 
from glob import glob 
import re

# os.chdir(r'C:\Users\ThanhTiem\Desktop\testpy')
txt = glob(r'D:\DDSM_KhoaLuanTN\CBIS-DDSM1\CBIS-DDSM\Calc-Training ROI and Cropped Images (DICOM)\Calc Train All Mask JPEGs Full\*txt')
print(len(txt))

# texts = []
# with open(txt_file, 'r', encoding='utf8') as fp:
#     for line in fp.readlines():
#         texts.append(line.strip())
nhan = []
a2 = []
a3 = []
a4 = []
a5 = []
for i in txt:
    with open(i,'r', encoding='utf-8') as f:
        text = f.read()
        arr = text.split(' ')