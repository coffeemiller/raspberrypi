import RPi.GPIO as GPIO             # GPIO 제어 모듈
import time                         # time 모듈

LED = 17                            # WPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
GPIO.setmode(GPIO.BCM)              # BCM모드 설정
GPIO.setup(LED, GPIO.OUT)           # OUTPUT(출력) 설정

try :                               # 정상 작동일 때
    while True :                    # 무한루프
        GPIO.output(LED, False)     # LED 꺼짐
        print("LED OFF...")         # "LED OFF..." 출력
        time.sleep(0.5)             # 0.5초 대기

        GPIO.output(LED, True)      # LED 켜짐
        print("LED ON...")          # "LED ON..." 출력
        time.sleep(0.5)             # 0.5초 대기

except :                            # 종료 시
    GPIO.cleanup()                  # GPIO 초기화
    print("end")