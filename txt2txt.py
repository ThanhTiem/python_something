import pandas as pd 
import re 
from glob import glob

txt = glob(r'D:\DDSM_KhoaLuanTN\CBIS-DDSM1\CBIS-DDSM\labels\*.txt')
# print(len(txt[0][:67]))
# print(txt[0])
# print(len(r'D:\DDSM_KhoaLuanTN\CBIS-DDSM1\CBIS-DDSM\labels\P_00001_LEFT_CC_MASK'))
for i in range(txt):
    # a = i[:67]
    print(i)