#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>

// wPi. 1, BCM. 18, Physical. 12
#define SERVO 1

// 서보모터의 각도는 -90도부터 90도까지 가능
static void Angle(int angle) {
    softPwmWrite(SERVO, 15 - angle / 10);
    printf("%dº\n", angle);
    delay(1000);
}

int main (void) {

    if (wiringPiSetup() == -1) { return 1; }

    softPwmCreate(SERVO, 0, 180);

    Angle(0);
    Angle(30);
    Angle(60);
    Angle(90);
    Angle(60);
    Angle(30);
    Angle(0);
    Angle(-30);
    Angle(-60);
    Angle(-90);
    Angle(-60);
    Angle(-30);
    Angle(0);
    
    return 0;
}