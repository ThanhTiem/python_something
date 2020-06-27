"""draw ground truth box"""
# pylint: disable-msg=C0103
import os
from glob import glob

import cv2
file_txt = r'D:\DDSM_KhoaLuanTN\testpy\new_label.txt'

with open(file_txt, 'r', encoding='utf-8') as f:
    text = f.readlines()
    for i in text:
        a = i.split(',')
        pathology = a[0].split('/')[-2]
        name = os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train',
                            pathology, a[0].split('/')[-1])
        # print(name)
        if 'Calc' in pathology:
            name_out = os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train',
                                    '_calc_train', a[0].split('/')[-1])
        if 'Mass' in pathology:
            name_out = os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train',
                                    '_mass_train', a[0].split('/')[-1])

        list_calc = [x.split('\\')[-1] for x in glob(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train\_calc_train\*')]
        list_mass = [x.split('\\')[-1] for x in glob(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train\_mass_train\*')]
        file_name = name.split('\\')[-1]

        if file_name in list_calc:
            name = os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train',
                                '_calc_train', a[0].split('/')[-1])
            name_out = name
        if file_name in list_mass:
            name = os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\textimg_calc_train',
                                '_mass_train', a[0].split('/')[-1])
            name_out = name

        # print(name)
        x = int(a[1])
        y = int(a[2])
        w = int(a[3])
        h = int(a[4])
        text = a[-1]
        print("aaaa: ", x, "-", y,"-", w, "-", h, "-",text )
        print("link: ", name_out)
       
        # print(name)
        img = cv2.imread(name)
        img = cv2.rectangle(img, (x, y), (w, h), (0, 0, 255), 3)
        if(text == "MALIGNANT\n"):
            img = cv2.putText(img, text, (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,  (0,0,255), 3)
        if(text == "BENIGN\n"):
            img = cv2.putText(img, text, (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,  (36,255,12), 3)
            
        # print(img)
        # img = cv2.copyMakeBorder(img, 0, 0, 0, 800, cv2.BORDER_CONSTANT, None, (0, 0, 0))
        cv2.imwrite(name_out, img)

# cv2.namedWindow('1', cv2.WINDOW_NORMAL)
# cv2.imshow('1', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
