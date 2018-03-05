import RPi.GPIO as GPIO

LED = 18                            # wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12

GPIO.setmode(GPIO.BCM)              # BCM 모드 설정
GPIO.setup(LED, GPIO.OUT)           # LED OUTPUT(출력) 설정

pwm = GPIO.PWM(LED, 1023)           # GPIO.PWM(BCM 번호, 최대값)
pwm.start(0)                        # pwm 초기값

try :
    while True :                    # 무한루프
        pwm.ChangeDutyCycle(20)     # ChangeDutyCycle(pwm값)

except :                            # 종료시
    pwm.stop()                      # pwm 중지
    GPIO.cleanup()                  # GPIO 초기화