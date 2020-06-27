import re
from glob import glob
import numpy as np 
import pandas as pd 
import os 


link_txt = glob(r'C:\Users\ThanhTiem\Desktop\testpy\labels\*')
print(len(link_txt))
a = []
# for file_txt in link_txt:
#     with open(file_txt,'r', encoding='utf-8') as f:
#         stri = f.readlines()
#         # print(stri)
#         a.append(stri)        
#         f.close()
#     # print(stri)
# print(len(a))

for file_txt in link_txt:
    b = []
    with open(file_txt) as fp:
        line = fp.read()
        line = line.strip("\n")
        print(file_txt)
        
        b.append(line)
        print(b)
        print("--------------")
    # with open(file_txt, 'w', encoding='utf-8') as fn:
    #     fn.write(b)  
    #     fn.close()
print("done!")
#file này code chưa tốt!!!!
