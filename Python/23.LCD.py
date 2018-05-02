#git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
#cd Adafruit_Python_CharLCD
#sudo python3 setup.py install

import Adafruit_CharLCD as LCD
import time, sys

#         LCD pin 1  > GND
#         LCD pin 2  > VCC 3.3v
#         LCD pin 3  > GND
rs = 21 # LCD pin 4  > BCM. 21, wPi. 29, Physical. 40
#         LCD pin 5  > GND
en = 20 # LCD pin 6  > BCM. 20, wPi. 28, Physical. 38
#         LCD pin 7  > X
#         LCD pin 8  > X
#         LCD pin 9  > X
#         LCD pin 10 > X
d4 = 16 # LCD pin 11 > BCM. 16, wPi. 27, Physical. 36
d5 = 12 # LCD pin 12 > BCM. 12, wPi. 26 Physical. 32
d6 = 1  # LCD pin 13 > BCM. 1, wPi. 31, Physical. 28
d7 = 7  # LCD pin 14 > BCM. 7, wPi. 11, Physical. 26
#         LCD pin 15 > VCC 3.3v
#         LCD pin 16 > GND

lcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, 16, 2, 2)

def StaticMessage(message) :
    lcd.message(message)
    time.sleep(3)
    lcd.clear()

def ShowCursor(message) :
    lcd.show_cursor(True)
    lcd.message(message)
    time.sleep(3)
    lcd.clear()
    lcd.show_cursor(False)

def BlinkCursor(message) :
    lcd.blink(True)
    lcd.message(message)
    time.sleep(3)
    lcd.clear()
    lcd.blink(False)

def ScrollRight(message) :
    lcd.message(message)
    for i in range(10):
        time.sleep(0.1)
        lcd.move_right()
    time.sleep(1)
    lcd.clear()

def ScrollLeft(message) :
    lcd.message(message)

    for i in range(10):
        lcd.move_right()

    for i in range(10):
        time.sleep(0.1)
        lcd.move_left()

    time.sleep(1)
    lcd.clear()

def LcdEnd(message) :
    lcd.message(message)
    time.sleep(3)
    lcd.clear()
    sys.exit(1)

if __name__ == "__main__" :
    try :
        StaticMessage("Hello World\nHello LCD")
        StaticMessage("Connection\nComplete!")
        ShowCursor("Show Cursor")
        BlinkCursor("Blink Cursor")
        ScrollRight("Scroll\nRight")
        ScrollLeft("Scroll\nLeft")
    except :
        lcd.clear()
        StaticMessage("You Press\nCtrl - C")
    finally :
        LcdEnd("Bye!")