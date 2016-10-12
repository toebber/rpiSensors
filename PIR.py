import RPi.GPIO as GPIO		#include the RPi.GPIO module. 

GPIO.setmode(GPIO.BOARD)	#Use pi board pin numbering

GPIO.setup(7, GPIO.IN)		#Set pin7 as input


print("Here we go - CTRL+C to exit")
try:
	while 1:
		if GPIO.input(7):
			print("motion detected")
			time.sleep(0.1)
		else:
			print("no activity")
			time.sleep(0.1)
except KeyboardInterrupt:	#If CTRL+C is pressed, exit cleanly
	GPIO.cleanup() 				#Garbage collection