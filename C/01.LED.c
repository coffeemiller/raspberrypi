#include <wiringPi.h>                       // wiringPi 헤더파일
#include <stdio.h>                          // stdio 헤더파일
#define LED 0                               // wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11

int main (void) {                            // 메인 함수 시작
    if (wiringPiSetup() == -1) {            // wiringPi를 불러오지 못했을 경우
        printf("setup wiringPi failed!");   // 에러로그 출력
        return 1;                           // 비정상 종료
    }

    pinMode(LED, OUTPUT);                   // OUTPUT(출력)으로 설정
    while (1) {                             // 무한루프
        digitalWrite(LED, LOW);             // LED 꺼짐
        printf("LED OFF...\n");             // 터미널에 "LED OFF..." 출력

        delay(500);                         // 500ms(0.5초) 대기
        
        digitalWrite(LED, HIGH);            // LED 켜짐
        printf("LED ON...\n");              // 터미널에 "LED ON..." 출력

        delay(500);                         // 500ms(0.5초) 대기
    }
    return 0;
}