# LED1 : DATA IN (저항 + GPIO 연결, 혹은 이전 LED의 DATA OUT으로부터 연결.)
# LED2 : 5V+
# LED3 : GND(가장 긴 것)
# LED4 : DATA OUT (다음 LED의 DATA IN으로 연결)

import neopixel, time, sys

LED_COUNT       = 8     # LED 갯수
LED_PIN         = 18    # BCM 18(Physical 12) (BCM 10(Physical 19) 일 땐 SPI 사용)
LED_BRIGHTNESS  = 255   # 0 ~ 255. 여러개 연결해서 파란색이 잘 나오지 않는 경우 조금씩 낮춰볼 것.
LED_CHANNEL     = 0     # 0일 땐 BCM 18(Physical 12), 1일 땐 BCM 13, 19, 41, 45, 53 연결 가능(Physical 33, 35)

def SetColor(strip, num, color, milli_sec) :    # 먼저 선언해야 색이 나옴.
    for i in range(milli_sec) :                 # 1초 = 1000
        strip.setPixelColor(num, color)         # LED 번호, neopixel.Color(r, g, b)
        strip.show()
        time.sleep(0.001)

strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, 800000, 10, False, LED_BRIGHTNESS, LED_CHANNEL, 1050624)
strip.begin()

def OneByOne() :
    for i in range(LED_COUNT) :
        if i % 3 == 1 :
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
        if i % 3 == 2 :
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
        if i % 3 == 0 :
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
            for j in range(256) :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green

def All() :
    for j in range(256) :
        for i in range(LED_COUNT) :
            if i % 3 == 1 :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
            if i % 3 == 2 :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green
            if i % 3 == 0 :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
    for j in range(256) :
        for i in range(LED_COUNT) :
            if i % 3 == 1 :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green
            if i % 3 == 2 :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
            if i % 3 == 0 :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
    for j in range(256) :
        for i in range(LED_COUNT) :
            if i % 3 == 1 :
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1)    # Green ~ Blue
            if i % 3 == 2 :
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1)    # Blue ~ Red
            if i % 3 == 0 :
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1)    # Red ~ Green

try :
    print("Ctrl-C 를 눌러 종료합니다.")

    while True :
        All()       # 전체가 한번에 색이 바뀜

        for i in range(LED_COUNT) :
            SetColor(strip, i, neopixel.Color(0, 0, 0), 1)  # Black(off)

        OneByOne()  # 하나씩 돌아가며 색이 바뀜

except :    # Press Ctrl-C
    print("\nCtrl-C를 누르셨습니다. 종료됩니다.")

    for i in range(LED_COUNT) :
        SetColor(strip, i, neopixel.Color(0, 0, 0), 1)  # Black(off)

    sys.exit(0)
