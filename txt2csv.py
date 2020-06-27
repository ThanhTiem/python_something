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
        nhan.append(arr[0])
        a2.append(arr[1])
        a3.append(arr[2])
        a4.append(arr[3])
        a5.append(arr[4])
        # print(arr)
# print(nhan)
# print(len(a2))
# print(len(a3))
# print(len(a4))
# print(len(a5))


df = pd.DataFrame()
df.insert(0,"label", nhan, True) 
df.insert(1,"x", a2, True)
df.insert( 2,"y", a3, True)
df.insert( 3,"w", a4, True)
df.insert( 4,"h", a5, True)
df.insert( 5,"path", txt, True)
# print(df)

tam = []
for i in df['h']:
    i = i[:-1]
    # print(i)
    tam.append(i)


df = df.drop('h', 1)
df.insert( 4,"h", tam, True)
print(df)
df.to_csv(r'C:\Users\ThanhTiem\Desktop\testpy\toado.csv')