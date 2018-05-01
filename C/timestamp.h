#include <stdio.h>
#include <time.h>

int timestamp(void){    // 시간을 출력하기 위한 모듈
    time_t time_now;
    struct tm *tm;
    time(&time_now);
    tm = localtime(&time_now);
    return (printf("%d-%02d-%02d %02d:%02d:%02d ", 
    tm->tm_year+1900, tm->tm_mon+1, tm->tm_mday, 
    tm->tm_hour, tm->tm_min, tm->tm_sec));
}