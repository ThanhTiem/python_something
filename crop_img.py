import cv2
from glob import glob
import os 
import xml.etree.ElementTree as ET
link_xml = glob(r'D:\DDSM_KhoaLuanTN\data_add_padding\Calc Train All Full JPEGs\*.xml')


for i in link_xml:
    name_jpg = i.split("\\")[-1].split(".")[-2] + ".jpg"
    link_jpg = i.split(".")[-2] + ".jpg"
    print(name_jpg)
    root = ET.parse(i).getroot()
    for type_tag in root.findall('object'):
        # name = type_tag.find('name').text
        xmin = type_tag.find('bndbox/xmin').text
        ymin = type_tag.find('bndbox/ymin').text
        xmax = type_tag.find('bndbox/xmax').text
        ymax = type_tag.find('bndbox/ymax').text
    img = cv2.imread(link_jpg)
    c = img[int(ymin):int(ymax), int(xmin):int(xmax)]
    cv2.imwrite(os.path.join(r'D:\DDSM_KhoaLuanTN\testpy\photo_crop\_calc_padding_crop', name_jpg), c)
    
