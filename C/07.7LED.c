#include <wiringPi.h>
#include <stdio.h>

#define LED1 0                       // wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
#define LED2 2                       // wPi. 2(GPIO. 2), BCM. 27, Physical-Pin. 13
#define LED3 3                       // wPi. 3(GPIO. 3), BCM. 22, Physical-Pin. 15
#define LED4 22                      // wPi. 22(GPIO. 22), BCM. 6, Physical-Pin. 31
#define LED5 23                      // wPi. 23(GPIO. 23), BCM. 13, Physical-Pin. 33
#define LED6 24                      // wPi. 24(GPIO. 24), BCM. 19, Physical-Pin. 35
#define LED7 25                      // wPi. 25(GPIO. 25), BCM. 26, Physical-Pin. 37

int main (void) {

    if (wiringPiSetup() == -1) return -1;

    unsigned char LED[7] = {LED1, LED2, LED3, LED4, LED5, LED6, LED7};  // 배열 안에 담아둠
    unsigned char i;
    unsigned char time = 100;

    for (i = 0 ; i < sizeof(LED) ; i++) {       // LED의 배열 크기만큼 반복
        pinMode(LED[i], OUTPUT);                // OUTPUT 설정
    }

    while (1) {                                 // 무한루프
        for (i = 0; i < sizeof(LED) ; i++) {    // LED의 배열 크기만큼 반복
            digitalWrite(LED[i], HIGH);         // LED[i] 켜짐
            delay(time);                        // time ms 대기
            digitalWrite(LED[i], LOW);          // LED[i] 꺼짐
            time--;                             // time = time - 1

            if (time <= 0) time = 100;          // time이 0이 되면 다시 time을 100으로 돌림
        }
    }
}