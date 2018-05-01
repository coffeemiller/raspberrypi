#include <wiringPi.h>
#include <stdio.h>
#include <time.h>

#define LIGHT 10 // wPi. 10, BCM. 8, Physical. 24(DOUT에 연결)

int timestamp(void){    // 시간을 출력하기 위한 모듈
    time_t time_now;
    struct tm *tm;
    time(&time_now);
    tm = localtime(&time_now);
    return (printf("%d-%02d-%02d %02d:%02d:%02d ", 
    tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday, 
    tm->tm_hour, tm->tm_min, tm->tm_sec));
}

int main(void) {
    if(wiringPiSetup() == -1){ return 1; }

    pinMode(LIGHT, INPUT);

    while(1) {
        timestamp();    // 시간 출력

        if(digitalRead(LIGHT) == HIGH) {
            printf("Dark\n");
        } else {
            printf("Light\n");
        }
        delay(1000);
    }

    return 0;
}