import cv2
from time import clock
def take_ref_image():
	cam=cv2.VideoCapture(0)
	cam.set(3,480)
	cam.set(4,360)
	#cam.set(10,150)
	#cam.set(11,160)
	#cam.set(12,80)
	for i in range(0,4):
		r,img=cam.read()
	img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img1=img1[90:360,:]
	cv2.imwrite("aref.jpg",img1)
	print("ref image captured")
	return
#take_ref_image()
