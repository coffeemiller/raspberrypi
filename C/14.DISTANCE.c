#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRIG 0  // wPi. 0, BCM. 17, Physical. 11
#define ECHO 1  // wPi. 1, BCM. 18, Physical. 12

void GetDistance() {
    int pulse_start, pulse_end;
    float distance;

    digitalWrite(TRIG, LOW);
    delay(500);

    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    while(digitalRead(ECHO) == 0) {
        pulse_start = micros();
    }
    while(digitalRead(ECHO) == 1) {
        pulse_end = micros();
    }

    distance = (pulse_end - pulse_start) / 29.0 / 2.0 / 100;
    printf("%.2fm\n", distance);
}

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
    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);

    while(1) {
        timestamp();
        GetDistance();
        delay(1000);
    }
    return 0;
}