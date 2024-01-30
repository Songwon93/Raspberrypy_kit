import RPi.GPIO as GPIO
import time

pin_RED = 4
pin_GREEN = 5
pin_BLUE = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_RED, GPIO.OUT)
GPIO.setup(pin_GREEN, GPIO.OUT)
GPIO.setup(pin_BLUE, GPIO.OUT)

def all_led_on():
    GPIO.output(pin_RED, 1)
    GPIO.output(pin_GREEN, 1)
    GPIO.output(pin_BLUE, 1)

def all_led_off():
    GPIO.output(pin_RED, 0)
    GPIO.output(pin_GREEN, 0)
    GPIO.output(pin_BLUE, 0)

def fade_in_out(pin, num):
    pwm = GPIO.PWM(pin, 100)
    pwm.start(0)
    try:
        for i in range(101):
            pwm.ChangeDutyCycle(i)
            time.sleep(num / 200)

        time.sleep(num)

        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(num / 200)
    finally:
        pwm.stop()

def mode_1():
    print("Mode 1: 모든 LED를 켭니다.")
    all_led_on()

def mode_2():
    print("Mode 2: 모든 LED를 끕니다.")
    all_led_off()

def mode_3():
    print("Mode 3: 빨간 LED가 3초 동안 밝아지고 어두워집니다.")
    fade_in_out(pin_RED, 3)

def mode_4():
    print("Mode 4: 초록 LED가 3초 동안 밝아지고 어두워집니다.")
    fade_in_out(pin_GREEN, 3)

def mode_5():
    print("Mode 5: 파란 LED가 3초 동안 밝아지고 어두워집니다.")
    fade_in_out(pin_BLUE, 3)

def mode_6():
    print("Mode 6: 사용자가 입력한 시간 동안 빨간, 초록, 파란 LED가 동시에 밝아지고 어두워집니다.")
    num = int(input("원하는 초를 입력하세요: "))
    
    pwm_red = GPIO.PWM(pin_RED, 100)
    pwm_green = GPIO.PWM(pin_GREEN, 100)
    pwm_blue = GPIO.PWM(pin_BLUE, 100)
    
    pwm_red.start(0)
    pwm_green.start(0)
    pwm_blue.start(0)
    
    try:
        for i in range(101):
            pwm_red.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i)
            pwm_blue.ChangeDutyCycle(i)
            time.sleep(num / 200)

        time.sleep(num)

        for i in range(100, -1, -1):
            pwm_red.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i)
            pwm_blue.ChangeDutyCycle(i)
            time.sleep(num / 200)
    finally:
        pwm_red.stop()
        pwm_green.stop()
        pwm_blue.stop()

def execute_mode(mode):
    modes = {
        1: mode_1,
        2: mode_2,
        3: mode_3,
        4: mode_4,
        5: mode_5,
        6: mode_6
    }
    selected_mode = modes.get(mode)
    if selected_mode:
        selected_mode()
    else:
        print("올바르지 않은 모드입니다.")

try:
    while True:
        mode = int(input("원하는 모드를 선택하세요 (1-6), 종료하려면 0을 입력하세요: "))
        if mode == 0:
            break
        execute_mode(mode)

finally:
    GPIO.cleanup()