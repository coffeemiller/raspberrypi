#include <wiringPi.h>
#include <softPwm.h>                // Software [Pulse Width Modulation] Module
#include <stdio.h>

#define R 0     // wPi. 0(GPIO. 0), BCM. 17, Physical-Pin. 11
#define G 1     // wPi. 1(GPIO. 1), BCM. 18, Physical-Pin. 12
#define B 2     // wPi. 2(GPIO. 2), BCM. 27, Physical-Pin. 13