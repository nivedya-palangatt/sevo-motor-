import RPi.GPIO as GPIO
import time
l=[4,14,15,17]
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
for i in l:
	GPIO.setup(i,GPIO.IN)

p=GPIO.PWM(18,50)
p.start(2.5)
while 1:
	if((GPIO.input(4)==0) or (GPIO.input(14)==0) or (GPIO.input(15)==0)):
		if(GPIO.input(17)==0):
			p.ChangeDutyCycle(12.5)
		else:
			p.ChangeDutyCycle(2.5)
	else:
		p.ChangeDutyCycle(2.5)
