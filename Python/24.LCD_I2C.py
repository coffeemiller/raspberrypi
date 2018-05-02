import time, sys
import i2c_module as I2C

# VCC > 5v
# GND
# SDA > Physical. 3, wPi. 8, BCM. 2
# SLC > Physical. 5, wPi. 9, BCM. 3

def StaticMessage(line1, line2) :
    I2C.lcd_init()  # 초기화
    I2C.lcd_string(line1, I2C.LCD_LINE_1)   # 윗줄
    I2C.lcd_string(line2, I2C.LCD_LINE_2)   # 아랫줄
    time.sleep(3)
    I2C.lcd_init()

def ScrollRight(line1, line2) :
    I2C.lcd_init()
    for i in range(10) :
        I2C.lcd_string("%s%s" % (" " * i, line1), I2C.LCD_LINE_1)
        I2C.lcd_string("%s%s" % (" " * i, line2), I2C.LCD_LINE_2)
        time.sleep(0.01)
    time.sleep(1)
    I2C.lcd_init()

def ScrollLeft(line1, line2) :
    I2C.lcd_init()
    for i in range(10) :
        I2C.lcd_string("%s%s" % (" " * (9 - i), line1), I2C.LCD_LINE_1)
        I2C.lcd_string("%s%s" % (" " * (9 - i), line2), I2C.LCD_LINE_2)
        time.sleep(0.01)
    time.sleep(1)
    I2C.lcd_init()

def LcdAbort() :
    I2C.lcd_init()  # 초기화
    I2C.lcd_string("   You Press    ", I2C.LCD_LINE_1)   # 윗줄
    I2C.lcd_string("    Ctrl - C    ", I2C.LCD_LINE_2)   # 아랫줄
    time.sleep(3)
    I2C.lcd_init()  # 초기화

def LcdEnd(line1, line2) :
    I2C.lcd_init()  # 초기화
    I2C.lcd_string(line1, I2C.LCD_LINE_1)   # 윗줄
    I2C.lcd_string(line2, I2C.LCD_LINE_2)   # 아랫줄
    time.sleep(3)
    I2C.lcd_init()  # 초기화
    sys.exit(1)

if __name__ == "__main__" :
    try :
        StaticMessage("Hello World!", "Hello LCD!")
        StaticMessage("Connection", "Complete!")
        ScrollRight("Scroll", "Right")
        ScrollLeft("Scroll", "Left")
    except :
        LcdAbort()
    finally :
        LcdEnd("      Bye!      ", "      Bye!      ")
