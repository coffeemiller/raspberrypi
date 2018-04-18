import RPi.GPIO as GPIO
import time

# wPi. 1, BCM. 18, Physical. 12
SERVO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, 50)
pwm.start(7.2)

# 각도는 -90도부터 90도까지 가능
def Angle(angle) :
    pwm.ChangeDutyCycle(7.2 - angle / 18.75)
    print("%sº" % angle)
    time.sleep(1)

# main문
if __name__ == "__main__" :
    try :
        Angle(0)
        Angle(30)
        Angle(60)
        Angle(90)
        Angle(60)
        Angle(30)
        Angle(0)
        Angle(-30)
        Angle(-60)
        Angle(-90)
        Angle(-60)
        Angle(-30)
        Angle(0)

    # Ctrl - c 또는 에러시
    except :
        print("ERROR")

    # 종료시
    finally :
        GPIO.cleanup()
        print("END")