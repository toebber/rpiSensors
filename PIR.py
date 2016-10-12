import RPi.GPIO as GPIO		#include the RPi.GPIO module. 
import time

pirPin = 7
pirState = 0

GPIO.setmode(GPIO.BOARD)	#Use pi board pin numbering
GPIO.setup(pirPin, GPIO.IN)		#Set pin7 as input


print("Here we go - CTRL+C to exit")
try:
	while 1:
		pirRead = GPIO.input(pirPin)		#read input value
		if pirRead:							#if value is true
			if pirState = 0				#we only want notification if the motion has just started
				print("motion detected")	
				pirState = 1				#set variable to note that motions has begun
		else:
			if pirState = 1				#if motion has begun --> 
				print("motion ended")		#and we no longe detect motion. Print motion ended
				pirState = 0
			#time.sleep(0.1)
except KeyboardInterrupt:	#If CTRL+C is pressed, exit cleanly
	GPIO.cleanup() 				#Garbage collection