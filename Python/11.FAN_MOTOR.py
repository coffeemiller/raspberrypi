import RPi.GPIO as GPIO
import time

FAN_IA = 23 # BCM. 23, wPi. 4, Physical. 16
FAN_IB = 24 # BCM. 24, wPi. 5, Physical. 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_IA, GPIO.OUT)
GPIO.setup(FAN_IB, GPIO.OUT)

# 왼쪽으로 2초 회전
def Left_2_Second() :
    GPIO.output(FAN_IA, True)
    GPIO.output(FAN_IB, False)
    time.sleep(2)

# 오른쪽으로 2초 회전
def Right_2_Second() :
    GPIO.output(FAN_IA, False)
    GPIO.output(FAN_IB, True)
    time.sleep(2)

# 정지상태로 2초 대기
def Wait_2_Second() :
    GPIO.output(FAN_IA, False)
    GPIO.output(FAN_IB, False)
    time.sleep(2)

# 파일 실행시 작동
if __name__ == "__main__" :
    try :
        # 무한루프
        while True :
            Left_2_Second()
            Wait_2_Second()
            Right_2_Second()
            Wait_2_Second()
            
    # Ctrl-C 종료시
    except :
        GPIO.cleanup()
        print("end")