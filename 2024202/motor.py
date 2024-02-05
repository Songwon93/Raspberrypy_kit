from gpiozero import Motor
import keyboard

# 모터 핀 세팅.
motorR = Motor(forward=12, backward=13)  # 모터 객체 생성.

try:
    while True:
        print("1: 전진 / 2: 후진 / 3: 잠시 스탑 / 4: 종료")
        key = keyboard.read_event(suppress=True).name

        if key == '1':
            # 전진
            motorR.forward(speed=0.7)
        elif key == '2':
            # 후진
            motorR.backward(speed=0.7)
        elif key == '3':
            # 잠시 정지
            motorR.stop()
            keyboard.read_event(suppress=True)  # 기다려서 키 떼는 것까지 받기 위해
        elif key == '4':
            # 종료
            break

except KeyboardInterrupt:
    # Ctrl+C를 눌러 프로그램을 중지할 경우
    pass

finally:
    # 모든 동작이 끝나면 모터 정지
    motorR.stop()