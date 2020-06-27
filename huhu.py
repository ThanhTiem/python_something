import cv2
import numpy as np

img = cv2.imread(r'C:\Users\ThanhTiem\Desktop\testpy\1_6.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 150, apertureSize=3)
# cv2.imshow("image", edges)
# cv2.waitKey(0)
minLineLength = 2
maxLineGap = 4
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 350, minLineLength, maxLineGap,10)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow("vcx",img)
cv2.waitKey(0)