import RPi.GPIO as GPIO                                     # GPIO 제어 모듈
import time                                                 # time 모듈

SWITCH = 18                                                 # Wpi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12
LED = 23                                                    # WPi. 4(GPIO. 4), BCM. 23, Physical-Pin. 16
GPIO.setmode(GPIO.BCM)                                      # BCM모드 설정
GPIO.setup(LED, GPIO.OUT)                                   # LED OUTPUT(출력) 설정
GPIO.setup(SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)   # SWITCH INPUT(입력)설정, 풀다운 저항 설정

try :                                                       # 정상 작동 상태
    while True :                                            # 무한루프
        if GPIO.input(SWITCH) == 1 :                        # 스위치를 눌렀을 때
            GPIO.output(LED, True)                          # LED ON
        else :                                              # 스위치를 누르지 않았을 때
            GPIO.output(LED, False)                         # LED OFF

except :                                                    # 종료 시
    GPIO.cleanup()                                          # GPIO 초기화
    print("end")