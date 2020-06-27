#source: https://medium.com/coinmonks/a-box-detection-algorithm-for-any-image-containing-boxes-756c15d7ed26


import cv2
import numpy as np 


def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


# path_image = r'C:\Users\ThanhTiem\Desktop\testpy\1_6.png'
path_image = r"C:\Users\ThanhTiem\Desktop\testpy\table2.jpg"
img = cv2.imread(path_image, 0)
(thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

img_bin = 255-img_bin 
# cv2.imwrite("Image_bin.jpg",img_bin)
# cv2.imshow("ijiji", img_bin)
# cv2.waitKey(0)


kernel_length = np.array(img).shape[1]//80
 
verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

# Weighting parameters, this will decide the quantity of an image to be added to make a new image.
alpha = 0.5
beta = 1.0 - alpha
# This function helps to add two image with specific weight parameter to get a third image as summation of two image.
img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
(thresh, img_final_bin) = cv2.threshold(img_final_bin, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite("img_final_bin.jpg",img_final_bin)


im2, contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Sort all the contours by top to bottom.
(contours, boundingBoxes) = sort_contours(contours, method="left-to-right")
# (contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")
# print(type(contours))
# print("------------------")
# print(type(im2))

idx = 0

boundary=[]
for c,cnt in enumerate(contours):
    # Returns the location and width,height for every contour
    x, y, w, h = cv2.boundingRect(cnt)
    boundary.append((x,y,w,h))
count=np.asarray(boundary)
max_width = np.sum(count[::, (0, 2)], axis=1).max()
max_height = np.max(count[::, 3])
nearest = max_height * 1.4
ind_list=np.lexsort((count[:,0],count[:,1]))
    # if (w < 1500 and (h > 20 and h <1000)):
    #     idx += 1
    #     new_img = img[y:y+h, x:x+w]
    #     cv2.imwrite('crop_'+str(idx) + '.png', new_img)
# # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
#     if (w > 80 and h > 20) and w > 3*h:
#         idx += 1
#         new_img = img[y:y+h, x:x+w]
#         cv2.imwrite('crop_'+str(idx) + '.png', new_img)

for c in ind_list:
    x, y, w, h = ind_list[c]
    if (w < 1500 and (h > 20 and h <1000)):
        idx += 1
        new_img = img[y:y+h, x:x+w]
        cv2.imwrite('crop_'+str(idx) + '.png', new_img)

# boundary=[]
# for c,cnt in enumerate(contours):
#     x,y,w,h = cv2.boundingRect(cnt)
#     boundary.append((x,y,w,h))
# count=np.asarray(boundary)
# max_width = np.sum(count[::, (0, 2)], axis=1).max()
# max_height = np.max(count[::, 3])
# nearest = max_height * 1.4
# ind_list=np.lexsort((count[:,0],count[:,1]))

# c=count[ind_list]

# print(c)