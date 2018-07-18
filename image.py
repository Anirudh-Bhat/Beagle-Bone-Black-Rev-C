import numpy
import cv2
from time import time
from time import sleep

def take_image():
	#starttime=time()
	cam=cv2.VideoCapture(0)
	cam.set(3,480)#width of the frame
	cam.set(4,360)#height -||-
	#cam.set(10,160)#brihtness
	#cam.set(11,150)#contrast
	#cam.set(12,128)#saturation
	for i in range(0,4):
		r,img=cam.read()
	cv2.imwrite("rawimg1.jpg",img)
	img=img[90:360,:]
	print("raw image 1")
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 	cv2.imwrite("raw_gray.jpg",img)
	print("raw to gray")
	bg=cv2.imread("aref.jpg",0)
	diff=img-bg
	cv2.imwrite("diff.jpg",diff)
	print("difference")
	kernel=numpy.ones((10,10),numpy.uint8)
	diff=cv2.morphologyEx(diff,cv2.MORPH_OPEN,kernel)
	r,diff=cv2.threshold(diff,127,255,cv2.THRESH_BINARY)
	cv2.imwrite("diff_binary.jpg",diff)
	print("final image")
	h,w=diff.shape
	t=h*w
	white=cv2.countNonZero(diff)
	t=float(white)/t
	cv2.imwrite("a.jpg",diff)
	#print(time()-starttime)
	print(int(t*100))
	return int(t*100) 
#take_image()
