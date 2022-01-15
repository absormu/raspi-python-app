import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

GPIO.output(16, GPIO.HIGH)  
sleep(1) 
GPIO.output(16, GPIO.LOW)

GPIO.cleanup()
