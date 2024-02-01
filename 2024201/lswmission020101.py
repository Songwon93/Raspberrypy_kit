import RPi.GPIO as GPIO
import time

buzzer = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

try:
    while True:
        pir_state = GPIO.input(27)
        if pir_state == True:
            GPIO.output(4, True)
            print("Motion Detected")
            
            # 부저를 1초 동안 울림
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(buzzer, GPIO.LOW)
            
        else:
            GPIO.output(4, False)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()