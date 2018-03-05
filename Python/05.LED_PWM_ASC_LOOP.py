import RPi.GPIO as GPIO
import time                             # delay 기능을 위한 모듈

LED = 18                                # wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12

GPIO.setmode(GPIO.BCM)                  # BCM 모드 설정
GPIO.setup(LED, GPIO.OUT)               # LED OUTPUT(출력) 설정

pwm = GPIO.PWM(LED, 1023)               # GPIO.PWM(BCM 번호, 최대값)
pwm.start(0)                            # pwm 초기값

try :
    while True :                        # 무한루프
        for value in range(0, 1024) :   # 0 <= value < 1024 반복문
            pwm.ChangeDutyCycle(value)  # ChangeDutyCycle(pwm값)
            time.sleep(0.005)           # 5ms(0.005초) 대기

except :                                # 종료 시
    pwm.stop()                          # pwm 중지
    GPIO.cleanup()                      # GPIO 초기화
    