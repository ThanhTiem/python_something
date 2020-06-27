import cv2
import numpy as np 
import math
from imutils.object_detection import non_max_suppression

def process_img(img):
    resize = cv2.resize(img, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def increase_brightness(img, value=30):
    # img = pre_processing1(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
def auto_brightness(img):
    H,W = img.shape[:2]
    brs = 0
    count = 0
    #10
    for i in range(0,H,5):
        for j in range(0,W,5):
            brs+= math.sqrt(0.241*(img[i,j,2]**2) + 0.691*(img[i,j,1]**2) + 0.068*(img[i,j,0]**2))
            count+=1
    avg=brs/count
    #160
    if(avg<180):
        v=int(180-avg)
        if v > 90 : v = 90
        img=increase_brightness(img,value=int(v))
    return img

def gray_scale(img):
    H,W = img.shape[:2]
    img = auto_brightness(img)
    gray = np.zeros((H,W), np.uint8)
    for i in range(H):
        for j in range(W):
        	#1.33
            graynum=int(1.43*img[i,j,1])+abs(int(img[i,j,1])-int(img[i,j,0])) 
            if(graynum>255):
                graynum=255
            gray[i][j]=graynum
    return gray

def redwave_filter(img):
    H,W = img.shape[:2]
    # img = auto_brightness(img)  
    gray = np.zeros((H,W), np.uint8)
    for i in range(H):
        for j in range(W):
            gray1 = int(1.45*img[i,j,2])+abs(int(img[i,j,2])-int(img[i,j,0])) #1.45
            gray2 = int(1.33*img[i,j,1])+abs(int(img[i,j,1])-int(img[i,j,0])) 
            if(gray1<gray2):
                graynum=gray2
            else:
                graynum=gray1
            if(graynum>255):
                graynum=255
                #sys.stderr.write(str(graynum))
            gray[i][j]=graynum
    return gray
def rotateImage(image, angle): 
    image_center = tuple(np.array(image.shape[1::-1])/2) 
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0) 
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR,borderValue=(255,255,255)) 
    return result 
def define_angle(x1,y1,x2,y2):
  #vector don vi ( 0,-1)
	cos_a = (y1-y2)/math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	angle = math.acos(cos_a)*180/math.pi
	if x2 < x1:
		return -angle
	else:
		return angle

def rotate(x, y, xm, ym, a):
	a = -a * math.pi/ 180
	xr = (x - xm) * math.cos(a) - (y - ym) * math.sin(a)   + xm
	yr = (x - xm) * math.sin(a) + (y - ym) * math.cos(a)   + ym
	xr = abs(xr)
	yr = abs(yr)
	return int(xr), int(yr)

def text_detection(image):
	orig = image.copy()
	(H, W) = image.shape[:2]

	(newW, newH) = (320, 320)
	rW = W / float(newW)
	rH = H / float(newH)

	# resize the image and grab the new image dimensions
	image = cv2.resize(image, (newW, newH))
	(H, W) = image.shape[:2]

	# define the two output layer names for the EAST detector model that
	# we are interested -- the first is the output probabilities and the
	# second can be used to derive the bounding box coordinates of text
	layerNames = [
		"feature_fusion/Conv_7/Sigmoid",
		"feature_fusion/concat_3"]

	net = cv2.dnn.readNet(r'D:\VNPT\TEST_Nhap\Yolo_detect\frozen_east_text_detection.pb')

	# construct a blob from the image and then perform a forward pass of
	# the model to obtain the two output layer sets
	blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
		(123.68, 116.78, 103.94), swapRB=True, crop=False)
	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)


	(numRows, numCols) = scores.shape[2:4]
	rects = []
	confidences = []

	# loop over the number of rows
	for y in range(0, numRows):
		# extract the scores (probabilities), followed by the geometrical
		# data used to derive potential bounding box coordinates that
		# surround text
		scoresData = scores[0, 0, y]
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y]

		# loop over the number of columns
		for x in range(0, numCols):
			# if our score does not have sufficient probability, ignore it
			if scoresData[x] < 0.3:
				continue

			# compute the offset factor as our resulting feature maps will
			# be 4x smaller than the input image
			(offsetX, offsetY) = (x * 4.0, y * 4.0)

			# extract the rotation angle for the prediction and then
			# compute the sin and cosine
			angle = anglesData[x]
			cos = np.cos(angle)
			sin = np.sin(angle)

			# use the geometry volume to derive the width and height of
			# the bounding box
			h = xData0[x] + xData2[x]
			w = xData1[x] + xData3[x]

			# compute both the starting and ending (x, y)-coordinates for
			# the text prediction bounding box
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h)

			# add the bounding box coordinates and probability score to
			# our respective lists
			rects.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])

	# apply non-maxima suppression to suppress weak, overlapping bounding
	# boxes
	boxes = non_max_suppression(np.array(rects), probs=confidences)

	MAX_y = 0
	MIN_y = orig.shape[0]
	MAX_X = 0
	MIN_X = orig.shape[1]
	for (startX, startY, endX, endY) in boxes:
		# scale the bounding box coordinates based on the respective
		startY = int(startY * rH)
		startX = int(startX * rW)
		endY = int(endY * rH)
		endX = int(endX * rW)

		if endY > MAX_y:
			MAX_y = endY
		if startY < MIN_y:
			MIN_y = startY
		if startX < MIN_X:
			MIN_X = startX
		if endX > MAX_X:
			MAX_X = endX
	if orig.shape[0] - MAX_y > 10:
		MAX_y += 10
	else:
		MAX_y = orig.shape[0]
	if orig.shape[1] - MAX_X > 20:
		MAX_X += 20
	else:
		MAX_X = orig.shape[1]
	if MIN_X < 15 :
		MIN_X = 0
	else:
		MIN_X = 10
	if MIN_y < 0:
		MIN_y = 0
	new_img = orig[MIN_y:MAX_y,:MAX_X]
	return new_img

# link = r'D:\VNPT\TEST_Nhap\Yolo_detect\1.jpg'
link = r'..\testpy\crop_29.png'
img = cv2.imread(link)

# a = cv2.copyMakeBorder(img, int(20), int(20), int(20), int(20), None, value=(255 ,255, 255) )
# b = text_detection(img)
img_process = redwave_filter(img)
cv2.imshow("redwave",img_process)

# cv2.waitKey(0)


cv2.imshow("a", img)
# cv2.imshow("border",  im)
cv2.waitKey(0)
