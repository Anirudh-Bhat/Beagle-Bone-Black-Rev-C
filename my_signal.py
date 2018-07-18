import Adafruit_BBIO.GPIO as GPIO
ng="P9_11"
nr="P9_12"
eg="P9_17"
er="P9_18"
sg="P9_23"
sr="P9_24"
wg="P9_27"
wr="P9_26"
import time

all=[ng,nr,sg,sr,eg,er,wg,wr]
for i in range(0,8):
	GPIO.setup(all[i],GPIO.OUT)
def ledon(pin):
	GPIO.output(pin,GPIO.HIGH)
	return
def ledoff(pin):
	GPIO.output(pin,GPIO.LOW)
	return
def northgreen():
		print("north green")
		ledon(ng)
		ledon(er)
		ledon(wr)
		ledon(sr)	
		ledoff(nr)
		ledoff(eg)
		ledoff(wg)
		ledoff(sg)
		return
def southgreen():
		print("south green")
		ledoff(ng)
		ledon(sg)
		ledoff(sr)
		ledon(er)
		ledon(wr)
		ledon(nr)	
		ledoff(eg)
		ledoff(wg)
		#time.sleep(1)
		return
def eastgreen():
		print("east green")
		ledoff(sg)
		ledon(sr)
		ledon(eg)
		ledoff(er)
		ledon(wr)
		ledon(nr)	
		ledoff(wg)
		ledoff(ng)
		#time.sleep(1)
		return
def westgreen():
		print("west green")	
		ledoff(eg)	
		ledon(wg)
		ledoff(wr)
		ledon(sr)
		ledon(er)
		ledon(nr)	
		ledoff(sg)
		ledoff(ng)
		#time.sleep(1)
		return	
	
	
	
def off():
	for i in range(0,8):
		ledoff(all[i])
	return

off()


	

	

	

	

	

	
	

	

	

	

	

	

	
