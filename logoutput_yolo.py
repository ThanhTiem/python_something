import os 
import re 

arr = []
with open(r'D:\DDSM_KhoaLuanTN\python_something\log_output.txt', 'r') as f:
    a = f.readlines()
for i in a:
    if 'avg' in i:
        arr.append(i)
print(len(arr))
for i in arr:
    # print(i)
    loss = i.split(',')[0].split(' ')[-1]
    loss_avg = i.split(',')[1].split(' ')[-2]
    print('loss: ', loss)
    print('loss_avg: ', loss_avg)