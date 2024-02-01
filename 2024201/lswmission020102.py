import RPi.GPIO as GPIO
import time

buzzer = 18
pin_RED = 4
pin_GREEN = 5
pin_BLUE = 6
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

GPIO.setmode(GPIO.BCM)

# GPIO 설정 및 PWM 초기화
GPIO.setup([pin_RED, pin_GREEN, pin_BLUE, buzzer], GPIO.OUT)
pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(1.0)

# 버튼 핀의 입력설정
GPIO.setup([button_pin1, button_pin2, button_pin3, button_pin4], GPIO.IN)

def play_tune(scale, twinkle, note_duration):
    for i in range(len(twinkle)):
        pwm.ChangeFrequency(scale[twinkle[i]])

        if i in [6, 13, 20, 27, 34, 41]:
            time.sleep(note_duration[i])  # 쉼표일 경우
        else:
            time.sleep(note_duration[i])  # 음표일 경우
        
# 버튼 처리 루프
try:
    while True:
        GPIO.output(pin_RED, 0)
        GPIO.output(pin_GREEN, 0)
        GPIO.output(pin_BLUE, 0)
        
        if GPIO.input(button_pin1) == GPIO.LOW:
            pwm.start(1.0)
            GPIO.output(pin_RED, 1)
            scale = [262, 294, 330, 349, 392, 440, 494]
            twinkle = [1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1,
                       5, 5, 4, 4, 3, 3, 2, 5, 5, 4, 4, 3, 3, 2,
                       1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1]
            note_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
                             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
                             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
            play_tune(scale, twinkle, note_duration)
            pwm.stop()
            
        elif GPIO.input(button_pin2) == GPIO.LOW:
            pwm.start(1.0)
            GPIO.output(pin_GREEN, 1)
            scale = [932, 1125, 1318, 1396, 1568, 1760, 1975]
            twinkle = [5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5,
                       6, 6, 5, 5, 3, 5, 3, 2, 3, 1]
            note_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5,
                             0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1]
            play_tune(scale, twinkle, note_duration)
            pwm.stop()
            
        elif GPIO.input(button_pin3) == GPIO.LOW:
            pwm.start(1.0)
            GPIO.output(pin_BLUE, 1)
            scale = [932, 1125, 1318, 1396, 1568, 1760, 1975]
            twinkle = [1, 3, 5, 1, 3, 5, 6, 6, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1]
            note_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 
                             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
            play_tune(scale, twinkle, note_duration)
            pwm.stop()
        elif GPIO.input(button_pin4) == GPIO.LOW:
            print("Button 4 pushed!")
            GPIO.output(pin_RED, 1)
            GPIO.output(pin_GREEN, 1)
            GPIO.output(pin_BLUE, 1)
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(buzzer, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()