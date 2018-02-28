#include <wiringPi.h>
#include <stdio.h>
#define SWITCH 1                            // Wpi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12
#define LED 4                               // WPi. 4(GPIO. 4), BCM. 23, Physical-Pin. 16

int main (void) {
    if (wiringPiSetup() == -1) {            // wiringPi를 불러오지 못했을 경우
        printf("setup wiringPi failed!");   // 에러로그 출력
        return 1;                           // 비정상 종료
    }

    pinMode(SWITCH, INPUT);                 // SWITCH를 INPUT으로 받아들임
    pinMode(SWITCH, PUD_DOWN);              // 풀다운 저항 설정
    pinMode(LED, OUTPUT);                   // LED는 OUTPUT으로 설정

    for (;;) {                              // 무한루프
        if (digitalRead(SWITCH) == 1) {     // SWITCH를 눌렀을 때
            digitalWrite(LED, HIGH);        // LED 켜짐
        } else {                            // SWITCH를 누르지 않고 있을 때
            digitalWrite(LED, LOW);         // LED 꺼짐
        }
    }
    return 0;
}