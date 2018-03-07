import RPi.GPIO as GPIO             # GPIO 제어 모듈
import time                         # time 모듈

LED1 = 17                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED2 = 27                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED3 = 22                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED4 = 6                            # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED5 = 13                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED6 = 19                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
LED7 = 26                           # wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11

LED = [LED1, LED2, LED3, LED4, LED5, LED6, LED7]
delay = 0.1                         # 100ms(0.1초)

GPIO.setmode(GPIO.BCM)              # BCM모드 설정

for i in LED :                      # LED의 크기만큼 반복
    GPIO.setup(i, GPIO.OUT)         # OUTPUT 설정
    
try :                               # 정상 작동일 때
    while True :                    # 무한루프
        for i in LED :              # LED의 크기만큼 반복
            GPIO.output(i, True)    # LED[i] 켜짐
            time.sleep(delay)       # delay초 대기
            GPIO.output(i, False)   # LED[i] 꺼짐
            
            delay -= 0.001          # delay = delay - 0.001

            if delay <= 0 :         # delay가 0이 되면(혹은 0보다 작으면)
                delay = 0.1         # 다시 원래 크기대로 복구
            
except :                            # 종료 시
    GPIO.cleanup()                  # GPIO 초기화
    print("end")