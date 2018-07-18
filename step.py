import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)

b = 0

def rotateClockWise(steps, off_time):

	global b
	for i in range(0,steps):	
		b = b + 1
		if(b>4):
			b=1

		if b == 1:
			GPIO.output("P8_9", GPIO.LOW)
			GPIO.output("P8_8", GPIO.HIGH)
			GPIO.output("P8_10", GPIO.LOW)
			GPIO.output("P8_7", GPIO.HIGH)

		if b == 2:
        	        GPIO.output("P8_7", GPIO.LOW)
                	GPIO.output("P8_8", GPIO.HIGH)
	                GPIO.output("P8_10", GPIO.LOW)
        	        GPIO.output("P8_9", GPIO.HIGH)

		if b == 3:
        	        GPIO.output("P8_7", GPIO.LOW)
                	GPIO.output("P8_9", GPIO.HIGH)
	                GPIO.output("P8_10", GPIO.HIGH)
        	        GPIO.output("P8_8", GPIO.LOW)

		if b == 4:
        	        GPIO.output("P8_7", GPIO.HIGH)
                	GPIO.output("P8_9", GPIO.LOW)
	                GPIO.output("P8_8", GPIO.LOW)
        	        GPIO.output("P8_10", GPIO.HIGH)
			
		time.sleep(off_time)
	print(str(steps)+" steps rotated clockwise")


def rotateCounterClockWise(steps, off_time):

	global b

        for i in range (0,steps):
                
                b=b+1

                if b > 4:
			b=1

                if b == 1:
                        GPIO.output("P8_7", GPIO.HIGH)
                        GPIO.output("P8_9", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.LOW)
                        GPIO.output("P8_10", GPIO.HIGH)

                if b == 2:
                        GPIO.output("P8_7", GPIO.LOW)
                        GPIO.output("P8_9", GPIO.HIGH)
                        GPIO.output("P8_10", GPIO.HIGH)
                        GPIO.output("P8_8", GPIO.LOW)

                if b == 3:
			GPIO.output("P8_7", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.HIGH)
                        GPIO.output("P8_10", GPIO.LOW)
                        GPIO.output("P8_9", GPIO.HIGH)

		if b == 4:
                        GPIO.output("P8_9", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.HIGH)
                        GPIO.output("P8_10", GPIO.LOW)
                        GPIO.output("P8_7", GPIO.HIGH)

		time.sleep(off_time)
	print(str(steps)+" steps rotated counterclockwise")
#while(1):
#rotateClockWise(24,0.010)
#time.sleep(1)
#	rotateCounterClockWise(24,0.010)
#	time.sleep(1)
