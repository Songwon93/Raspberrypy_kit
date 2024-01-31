import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(10.0)  # 듀티비를 50%로 설정함

# ==작은별 계이름 ==
# 4 옥타브: 도(1)/ 레(2)/ 미(3)/ 파(4)/ 솔(5)/ 라(6)/ 시(7)
scale = [932, 1125, 1318, 1396, 1568, 1760, 1975]

# 작은별 악보
twinkle = [1, 3, 5, 1, 3, 5, 6, 6, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1]
# 각 음표와 쉼표의 지속 시간
note_duration = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 
                 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]

try:
    for i in range(len(twinkle)):
        pwm.ChangeFrequency(scale[twinkle[i]])

        if  i == 10:
            time.sleep(note_duration[i])  # 쉼표일 경우
        else:
            time.sleep(note_duration[i])  # 음표일 경우

finally:
    pwm.stop()
    GPIO.cleanup()