import numpy as np 
import pandas as pd 
import os 
import re 
from glob import glob

list_txt = glob(r'C:\Users\ThanhTiem\Desktop\testpy\labels\*.txt')

for file_txt in list_txt:
    with open(file_txt,'r', encoding='utf-8') as f:
        stri = f.read()
        # a = stri.replace('\n15 ', '\n0 ')
        # a = "0"+stri[2:]
        f.close()
    print(stri)
    # print(a)
    # print("-------")
    # with open(file_txt, 'w', encoding='utf-8') as fn:
    #     fn.write(a)    
    #     fn.close()
print('done!')

