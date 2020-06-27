import pandas as pd 
import re 
from glob import glob

a = glob(r'D:\DDSM_KhoaLuanTN\darknet\data\images\*.jpg')

# for i in a:
#     stri = i + '\n'
#     with open('train.txt','a', encoding='utf-8') as f:
#         f.writelines(stri)

# print(len(a))

#-------------------------------------
import random
b = random.sample(a, 484)
X = []
for i in b:
    stri = i + '\n'
    with open('val.txt','a', encoding='utf-8') as f:
        f.writelines(stri)
    X.append(i)
tam = []
# for l in a:
#     for j in X:
#         if(l != j):
#             tam.append(l)
# for k in tam:
#     stri = k + '\n'
#     with open('train.txt','a', encoding='utf-8') as f:
#         f.writelines(stri)
# print('done!')

#----------------------------------------------

for l in a:
    if(l not in X):
       tam.append(l)

for k in tam:
    stri = k + '\n'
    with open('train.txt','a', encoding='utf-8') as f:
        f.writelines(stri)
print('done!')