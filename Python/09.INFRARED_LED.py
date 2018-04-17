import RPi.GPIO as GPIO

INFRARED = 7    # BCM. 7(wPi. 11, Physical. 26)
LED = 18        # BCM. 10(wPi. 12, Physical. 19)

GPIO.setmode(GPIO.BCM)
GPIO.setup(INFRARED, GPIO.IN)   # 적외선 센서는 '감지' 센서이므로 INPUT으로 한다.
GPIO.setup(LED, GPIO.OUT)

try :
    while True :
        if GPIO.input(INFRARED) == 1 :  # 적외선 센서가 '감지' 했을 때
            GPIO.output(LED, True)
        else :                          # 적외선 센서에 아무것도 감지되지 않을 때
            GPIO.output(LED, False)

except :            # Ctrl - C로 종료시
    GPIO.cleanup()
    print("end")