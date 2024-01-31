import RPi.GPIO as GPIO
import time
import random

pin_RED = 4
pin_GREEN = 5
pin_BLUE = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_RED, GPIO.OUT)
GPIO.setup(pin_GREEN, GPIO.OUT)
GPIO.setup(pin_BLUE, GPIO.OUT)

class RestartLoop(Exception):
    pass

def collect_color():
    while True:
        random_1color = random.randint(1, 3)
        A = random_1color
        random_2color = random.randint(1, 3)
        B = random_2color

        if A != B:
            break

    C = None  # 초기값 설정

    if A == 1:
        if B == 1:
            C = 4
            print("정답이 없습니다\n")
        elif B == 2:
            C = 1
            GPIO.output(pin_RED, 1)
            GPIO.output(pin_GREEN, 1)
            time.sleep(3)
            GPIO.output(pin_RED, 0)
            GPIO.output(pin_GREEN, 0)
        elif B == 3:
            C = 2
            GPIO.output(pin_RED, 1)
            GPIO.output(pin_BLUE, 1)
            time.sleep(3)
            GPIO.output(pin_RED, 0)
            GPIO.output(pin_BLUE, 0)
    elif A == 2:
        if B == 2:
            C = 4
            print("정답이 없습니다\n")
        elif B == 1:
            C = 3
            GPIO.output(pin_BLUE, 1)
            GPIO.output(pin_GREEN, 1)
            time.sleep(3)
            GPIO.output(pin_BLUE, 0)
            GPIO.output(pin_GREEN, 0)
        elif B == 3:
            C = 2
            GPIO.output(pin_RED, 1)
            GPIO.output(pin_BLUE, 1)
            time.sleep(3)
            GPIO.output(pin_RED, 0)
            GPIO.output(pin_BLUE, 0)
    elif A == 3:
        if B == 3:
            C = 4
            print("정답이 없습니다\n")
        elif B == 1:
            C = 1
            GPIO.output(pin_GREEN, 1)
            GPIO.output(pin_RED, 1)
            time.sleep(3)
            GPIO.output(pin_GREEN, 0)
            GPIO.output(pin_RED, 0)
        elif B == 2:
            C = 3
            GPIO.output(pin_RED, 1)
            GPIO.output(pin_BLUE, 1)
            time.sleep(3)
            GPIO.output(pin_RED, 0)
            GPIO.output(pin_BLUE, 0)

    return A, B, C

def mode_1():
    print("게임을 시작합니다")

    while True:
        try:
            A, B, C = collect_color()
        except RestartLoop:
            continue

        answer = int(input("정답을 기입하시오.\n1.노랑\n2.마젠타\n3.시안\n4.정답이 없습니다\n"))

        if C == answer:
            print("정답 입니다!")
            for color_pin in [pin_RED, pin_GREEN, pin_BLUE]:
                GPIO.output(color_pin, 1)
                time.sleep(1)
                GPIO.output(color_pin, 0)
                time.sleep(1)
            break

        elif C != answer:
            print("틀렸습니다", C)
            for _ in range(3):
                GPIO.output(pin_RED, 1)
                time.sleep(1)
                GPIO.output(pin_RED, 0)
                time.sleep(1)
            break

def execute_mode(mode):
    modes = {
        1: mode_1
    }
    selected_mode = modes.get(mode)
    if selected_mode:
        selected_mode()
    else:
        print("올바르지 않은 모드입니다.")

try:
    while True:
        print("================\n")
        print("빛의 삼원색 게임\n")
        print("================\n")
        mode = int(input("원하는 시작하려면 1번을 누르시오, 종료하려면 0을 입력하세요: "))
        if mode == 0:
            break
        execute_mode(mode)

finally:
    GPIO.cleanup()