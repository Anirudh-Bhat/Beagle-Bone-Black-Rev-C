import time
import refimg
import image
import step
starttime=time.time()
refimg.take_ref_image()
a=[0,0,0,0]
def main_module():
	for i in range(0,4):
		a[i]=image.take_image()
		if(i<3):
			step.rotateClockWise(24,0.010)
			time.sleep(1)	
	step.rotateCounterClockWise(72,0.010)

main_module()
#print(a)
cycle_time=60	#input("input cycle time ")
sum1=sum(a)
#print(sum1)
for i in range(0,4):
	if(i==0):
		a[i]=int((float(a[i])/sum1)*cycle_time)
	else:
		a[i]=a[i-1]+int((float(a[i])/sum1)*cycle_time)
a=[2,18,48]
print(a)
start_time=time.time()
import my_signal
while(time.time()-start_time<cycle_time):
	#print(time.time()-start_time)
	if(int(time.time()-start_time)==0):
		my_signal.northgreen()
	if(int(time.time()-start_time)==a[0]):
		my_signal.eastgreen()
	if(int(time.time()-start_time)==a[1]):
		my_signal.southgreen()
	if(int(time.time()-start_time)==a[2]):
		my_signal.westgreen()




