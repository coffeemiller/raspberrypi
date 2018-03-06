import RPi.GPIO as GPIO
import time                             # delay 기능을 위한 모듈

LED = 18                                # wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12

GPIO.setmode(GPIO.BCM)                  # BCM 모드 설정
GPIO.setup(LED, GPIO.OUT)               # LED OUTPUT(출력) 설정

pwm = GPIO.PWM(LED, 10)                 # GPIO.PWM(BCM 번호, Hz)
pwm.start(0)                            # pwm 초기값

for value in range(0, 1024) :           # 0 <= value < 1024 반복문
    pwm.ChangeDutyCycle(value / 10.23)  # ChangeDutyCycle(0 ~ 100)
    time.sleep(0.005)                   # 5ms(0.005초) 대기

pwm.stop()                              # pwm 중지
GPIO.cleanup()                          # GPIO 초기화