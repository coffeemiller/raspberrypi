#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>   // Speaker모듈에 Digital신호를 주기 위한 헤더파일

#define SPEAKER 6   // GPIO. 6(Physical. 22)

#define C 261.63    // 도
#define D 293.66    // 레
#define E 329.63    // 미
#define F 349.23    // 파
#define G 391.00    // 솔
#define A 440.00    // 라

float notes[][2] = {    // 3차원배열. {음계, 음표} 이렇게 들어감.
    {G, 8}, {G, 8}, {A, 8}, {A, 8}, {G, 8}, {G, 8}, {E, 4},
    {G, 8}, {G, 8}, {E, 8}, {E, 8}, {D, 2},
    {G, 8}, {G, 8}, {A, 8}, {A, 8}, {G, 8}, {G, 8}, {E, 4},
    {G, 8}, {E, 8}, {D, 8}, {E, 8}, {C, 2}
};

int main(void){
    if(wiringPiSetup() == -1){return -1;}

    softToneCreate(SPEAKER);                    // Speaker 모듈 선언

    for (int i = 0 ; i < sizeof(notes) ; i++) { // notes배열 수 만큼 반복
        softToneWrite(SPEAKER, notes[i][0]);    // notes[i]번째의 음계를 소리를
        delay(4 / notes[i][1] * 1000 - 10);     // notes[i]번째의 음표만큼 지속함.
        softToneWrite(SPEAKER, 0);              // 소리를 멈추고
        delay(10);                              // 0.01초의 간격을 둠.
    }

    return 0;
}
