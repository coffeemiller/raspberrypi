import RPi.GPIO as GPIO

LED = 18                            # wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12

GPIO.setmode(GPIO.BCM)              # BCM 모드 설정
GPIO.setup(LED, GPIO.OUT)           # LED OUTPUT(출력) 설정

pwm = GPIO.PWM(LED, 10)             # GPIO.PWM(BCM 번호, Frequency(Hz))
pwm.start(0)                        # Duty Cycle = 0%

try :                               # 정상 작동시
    while True :                    # 무한루프
        pwm.ChangeDutyCycle(50)     # ChangeDutyCycle(0 ~ 100)

except :                            # 종료시
    pwm.stop()                      # pwm 중지
    GPIO.cleanup()                  # GPIO 초기화