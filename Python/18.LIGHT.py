import RPi.GPIO as GPIO
import time

LIGHT = 8  # BCM. 8, wPi. 10, Physical. 24(DOUT에 연결)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT, GPIO.IN)

if __name__ == "__main__" :
    try :
        while(1) :
            now = time.localtime()
            timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
            (now.tm_year, now.tm_mon, now.tm_mday, 
            now.tm_hour, now.tm_min, now.tm_sec))
            if GPIO.input(LIGHT) == 1 : # 빛이 없을 때
                print(timestamp, "Dark")
            else :                      # 빛이 감지될 때
                print(timestamp, "Light")
            time.sleep(1)
    except :
        print("err or Ctrl - C")
    finally :
        GPIO.cleanup()
        print("END")