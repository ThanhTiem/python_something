import cv2
import numpy as np 
import camelot


path = r'C:\Users\ThanhTiem\Desktop\testpy\table.pdf'
table = camelot.read_pdf(path)
table.export(r'C:\Users\ThanhTiem\Desktop\testpy\out.csv', f='csv', compress=True) 
# table[0]
# table.to_csv('foo.csv')
#test nhan thay k thanh cong! loai pp nay