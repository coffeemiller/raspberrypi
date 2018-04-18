import RPi.GPIO as GPIO
import time

# BCM. 23, wPi. 4, Physical. 16
FAN_IA = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_IA, GPIO.OUT)

pwm = GPIO.PWM(FAN_IA, 60)
pwm.start(0)

# 미풍
def Weak() :
    pwm.ChangeDutyCycle(66)
    print("미풍")
    time.sleep(5)

# 약풍
def Medium() :
    pwm.ChangeDutyCycle(33)
    print("약풍")
    time.sleep(5)

# 약풍
def Strong() :
    pwm.ChangeDutyCycle(0)
    print("강풍")
    time.sleep(5)

# 파일 실행시 작동
if __name__ == "__main__" :
    try :
        # 무한루프
        while True :
            Weak()
            Medium()
            Strong()
            
    # Ctrl-C 종료시
    except :
        GPIO.cleanup()
        print("end")