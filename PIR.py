import RPi.GPIO as GPIO		#include the RPi.GPIO module. 
import time

pirPin = 7

GPIO.setmode(GPIO.BOARD)	#Use pi board pin numbering
GPIO.setup(pirPin, GPIO.IN)		#Set pin7 as input


print("Here we go - CTRL+C to exit")
try:
	while 1:
		if GPIO.input(pirPin):
			print("motion detected")
			time.sleep(0.1)
		else:
			print("no activity")
			time.sleep(0.1)
except KeyboardInterrupt:	#If CTRL+C is pressed, exit cleanly
	GPIO.cleanup() 				#Garbage collection