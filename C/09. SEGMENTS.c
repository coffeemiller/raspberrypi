#include <stdio.h>
#include <wiringPi.h>

#define A 13    // GPIO. 13 (Physical. 21)
#define B 14    // GPIO. 14 (Physical. 23)
#define C 4     // GPIO. 4  (Physical. 16)
#define D 5     // GPIO. 5  (Physical. 18)
#define E 21    // GPIO. 21 (Physical. 29)
#define F 22    // GPIO. 22 (Physical. 31)
#define G 23    // GPIO. 23 (Physical. 33)

unsigned char SEGMENTS[7] = {A, B, C, D, E, F, G};
unsigned int NUMBER[10][7] = {
    {0, 0, 0, 0, 0, 0, 1},  // 0
    {1, 0, 0, 1, 1, 1, 1},  // 1
    {0, 0, 1, 0, 0, 1, 0},  // 2
    {0, 0, 0, 0, 1, 1, 0},  // 3
    {1, 0, 0, 1, 1, 0, 0},  // 4
    {0, 1, 0, 0, 1, 0, 0},  // 5
    {0, 1, 0, 0, 0, 0, 0},  // 6
    {0, 0, 0, 1, 1, 1, 1},  // 7
    {0, 0, 0, 0, 0, 0, 0},  // 8
    {0, 0, 0, 0, 1, 0, 0}   // 9
};

int main(void){
    if(wiringPiSetup() == -1){return 1;}

    // 반복문을 이용하여 OUTPUT 설정
    for (int i = 0 ; i < 7 ; i++) {
        pinMode(SEGMENTS[i], OUTPUT);
    }

    while(1) {
        // 0~9까지 0.5초씩 번갈아가며 출력
        for (int i = 0 ; i < 10 ; i++) {
            for (int j = 0 ; j < 7 ; j++) {
                digitalWrite(SEGMENTS[j], NUMBER[i][j]);
            }
            delay(500);
        }
    }
}
