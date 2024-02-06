import RPi.GPIO as GPIO
import time

servo_pin = 14
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

servo_min_duty = 3
servo_max_duty = 12
current_deg = 90

def set_servo_degree(degree):
    GPIO.setup(servo_pin, GPIO.OUT)
    past_time = time.time()

    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0

    duty = servo_min_duty + (degree * (servo_max_duty - servo_min_duty) / 180.0)
    servo.ChangeDutyCycle(duty)

    while True:
        current_time = time.time()
        if current_time - past_time > 0.5:
            break

    GPIO.setup(servo_pin, GPIO.IN)
    return degree

try:
    while True:
        if GPIO.input(button_pin1) == GPIO.LOW:
            set_servo_degree(45)
        elif GPIO.input(button_pin2) == GPIO.LOW:
            set_servo_degree(90)
        elif GPIO.input(button_pin3) == GPIO.LOW:
            set_servo_degree(180)
        elif GPIO.input(button_pin4) == GPIO.LOW:
            set_servo_degree(100)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()