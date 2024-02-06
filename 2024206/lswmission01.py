import RPi.GPIO as GPIO
import time

pin_RED = 4
pin_GREEN = 5
pin_BLUE = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_RED, GPIO.OUT)
GPIO.setup(pin_GREEN, GPIO.OUT)
GPIO.setup(pin_BLUE, GPIO.OUT)

i = 0

for i in range(10):
	GPIO.output(pin_RED, 1)
	time.sleep(0.5)
	GPIO.output(pin_RED, 0)
	time.sleep(0.5)
	GPIO.output(pin_GREEN, 1)
	time.sleep(0.5)
	GPIO.output(pin_GREEN, 0)
	time.sleep(0.5)
	GPIO.output(pin_BLUE, 1)
	time.sleep(0.5)
	GPIO.output(pin_BLUE, 0)
	time.sleep(0.5)


GPIO.cleanup()


