#include "LCD_I2C.h"

// GND
// VCC  5v
// SDA  Physical. 3, wPi. 8, BCM. 2
// SCL  Physical. 5, wPi. 9, BCM. 3

void StaticMessage(char line1[], char line2[]) {
    lcdLoc(LINE1);
    typeln(line1);
    lcdLoc(LINE2);
    typeln(line2);
    delay(3000);
    ClrLcd();
}

void ScrollRight(char line1[], char line2[]) {
    char whitespace[20] = " ";
    for(char i = 0 ; i < 10 ; i++) {
        ClrLcd();
        lcdLoc(LINE1);
        for(char j = 0 ; j < i ; j++) {
            typeln(" ");
        }
        typeln(line1);
        lcdLoc(LINE2);
        for(char j = 0 ; j < i ; j++) {
            typeln(" ");
        }
        typeln(line2);
        delay(10);
    }
    delay(1000);
    ClrLcd();
}

void ScrollLeft(char line1[], char line2[]) {
    for(char i = 0 ; i < 10 ; i++) {
        ClrLcd();
        lcdLoc(LINE1);
        for(char j = 9 ; j > i ; j--) {
            typeln(" ");
        }
        typeln(line1);
        lcdLoc(LINE2);
        for(char j = 9 ; j > i ; j--) {
            typeln(" ");
        }
        typeln(line2);
        delay(10);
    }
    delay(1000);
    ClrLcd();
}

void LcdEnd() {
    ClrLcd();
    lcdLoc(LINE1);
    typeln("      BYE!      ");
    lcdLoc(LINE2);
    typeln("      BYE!      ");
    delay(3000);
    ClrLcd();
}

int main(void) {
    if(wiringPiSetup() == -1){ return 1; }
    fd = wiringPiI2CSetup(I2C_ADDR);

    lcd_init();
    
    StaticMessage("Hello, World!", "Hello, LCD!");
    StaticMessage("Connection", "Complete!");
    ScrollRight("Scroll", "Right");
    ScrollLeft("Scroll", "Left");
    LcdEnd();
    return 0;
}

// gcc -o LCD_I2C LCD_I2C.c -lwiringPi -lwiringPiDev