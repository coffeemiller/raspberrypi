import RPi.GPIO as GPIO

INFRARED = 7    # BCM. 7(wPi. 11, Physical. 26)
BUZZER = 17     # BCM. 17(wPi. 0, Physical. 11)
LED = 18        # BCM. 18(wPi. 1, Physical. 12)

GPIO.setmode(GPIO.BCM)
GPIO.setup(INFRARED, GPIO.IN)   # 적외선 센서는 '감지' 센서이므로 INPUT으로 한다.
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

try :
    while True :
        if GPIO.input(INFRARED) == 1 :  # 적외선 센서가 '감지' 했을 때
            GPIO.output(BUZZER, True)
            GPIO.output(LED, True)
        else :                          # 적외선 센서에 아무것도 감지되지 않을 때
            GPIO.output(BUZZER, False)
            GPIO.output(LED, False)

except :            # Ctrl - C로 종료시
    GPIO.cleanup()
    print("end")