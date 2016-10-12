import RPi.GPIO as GPIO		#include the RPi.GPIO module. 

GPIO.setmode(GPIO.BOARD)	#Use pi board pin numbering

GPIO.setup(7.GPIO.IN)		#Set pin7 as input

if GPIO.input(7):
	print("motion detected")
else:
	print("no activity")

