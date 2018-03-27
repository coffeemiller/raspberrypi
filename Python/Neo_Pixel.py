# LED1 : DATA IN (GPIO 연결, 혹은 이전 LED의 DATA OUT으로부터 연결.)
# LED2 : 5V+ (저항 + 콘덴서)
# LED3 : GND (콘덴서)
# LED4 : DATA OUT (다음 LED의 DATA IN으로 연결)

import neopixel, time, sys

LED_COUNT       = 3     # LED 갯수
LED_PIN         = 19    # BCM 19(Physical 35) (BCM 10(Physical 19) 일 땐 SPI 사용)
LED_BRIGHTNESS  = 255   # 0 ~ 255. 여러개 연결해서 파란색이 잘 나오지 않는 경우 조금씩 낮춰볼 것.
LED_CHANNEL     = 1     # 0일 땐 BCM 18(Physical 12), 1일 땐 BCM 13, 19, 41, 45, 53 연결 가능(Physical 33, 35)

def SetColor(strip, num, color, milli_sec) :    # 먼저 선언해야 색이 나옴.
    for i in range(milli_sec) :                 # 1초 = 1000
        strip.setPixelColor(num, color)         # LED 번호, neopixel.Color(r, g, b)
        strip.show()
        time.sleep(0.001)

strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, 800000, 10, False, LED_BRIGHTNESS, LED_CHANNEL, 1050624)
strip.begin()

def R_G_B() :
    for i in range(neopixel.numPixels()) :
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

try :
    print("Ctrl-C 를 눌러 종료합니다.")

    while True :
        R_G_B()
            

except :    # Press Ctrl-C
    print("\nCtrl-C를 누르셨습니다. 종료됩니다.")

    for i in range(strip.numPixels()) :
        SetColor(strip, i, neopixel.Color(0, 0, 0), 1)  # Black(off)

    sys.exit(0)
