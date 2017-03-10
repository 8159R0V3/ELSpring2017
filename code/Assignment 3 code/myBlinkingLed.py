#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def Blink():
	x = 1
	while True:
		for i in range(0,3):
			print "blink #" + str(i+1)
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
		time.sleep(5)
		for i in range(0,4):
			print "blink #" + str(i+1)
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
		time.sleep(5)
	print "done!!"
	GPIO.cleanup()

Blink()
