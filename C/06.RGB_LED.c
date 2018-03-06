#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

#define uchar unsigned char

#define R 0     // wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11(LED 4)
#define G 1     // wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12(LED 2)
#define B 2     // wPi. 2(GPIO. 2), BCM. 27, Physical-Pin. 13(LED 1)
                // 가장 긴 핀(LED 3)은 Phisical-Pin. 1(3.3v)로 연결

// 0xff = 255
void SetLed (void) {
    softPwmCreate(R, 0, 255);
    softPwmCreate(G, 0, 255);
    softPwmCreate(B, 0, 255);
}

// 공통캐소드라서 값을 반대로 넣어줘야함
void LedColorSet (uchar r, uchar g, uchar b) {
    softPwmWrite(R, 0xff - r);
    softPwmWrite(G, 0xff - g);
    softPwmWrite(B, 0xff - b);
}

int main (void) {

    if (wiringPiSetup() == -1) return -1;

    SetLed();   // 앞에 선언한 함수 호출

    while (1) {                          // 무한루프
        LedColorSet(0xff, 0x00, 0x00);   // Red (ff0000)
        delay(1000);
        LedColorSet(0x00, 0xff, 0x00);   // Green (00ff00)
        delay(1000);
        LedColorSet(0x00, 0x00, 0xff);   // Blue (0000ff)
        delay(1000);
        LedColorSet(0xff, 0xff, 0xff);   // White (ffffff)
        delay(1000);
        LedColorSet(0x00, 0xff, 0xff);   // Cyan (00ffff)
        delay(1000);
        LedColorSet(0xff, 0x00, 0xff);   // Magenta (ff00ff)
        delay(1000);
        LedColorSet(0xff, 0xff, 0x00);   // Yellow (ffff00)
        delay(1000);
        LedColorSet(0x00, 0x00, 0x00);   // Black(꺼짐) (000000)
        delay(1000);
        LedColorSet(0xff, 0xa2, 0x00);   // Orange (ffa200)
        delay(1000);
        LedColorSet(0xff, 0x7d, 0xe5);   // Pink (ff7de5)
        delay(1000);
    }
}