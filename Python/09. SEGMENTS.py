import RPi.GPIO as GPIO
import time

A = 9   # BCM. 9  (Physical. 21)
B = 11  # BCM. 11 (Physical. 23)
C = 23  # BCM. 23 (Physical. 16)
D = 24  # BCM. 24 (Physical. 18)
E = 5   # BCM. 5  (Physical. 29)
F = 6   # BCM. 6  (Physical. 31)
G = 13  # BCM. 13 (Physical. 33)

SEGMENTS = [A, B, C, D, E, F, G]
NUMBER = [
    [0, 0, 0, 0, 0, 0, 1],  # 0
    [1, 0, 0, 1, 1, 1, 1],  # 1
    [0, 0, 1, 0, 0, 1, 0],  # 2
    [0, 0, 0, 0, 1, 1, 0],  # 3
    [1, 0, 0, 1, 1, 0, 0],  # 4
    [0, 1, 0, 0, 1, 0, 0],  # 5
    [0, 1, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 1, 1, 1, 1],  # 7
    [0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 1, 0, 0]   # 9
]

GPIO.setmode(GPIO.BCM)
# 반복문을 이용하여 OUT 설정
for i in range(7) :
    GPIO.setup(SEGMENTS[i], GPIO.OUT)

try :
    while True :
        # 0~9까지 0.5초씩 번갈아가며 출력
        for i in range(10) :
            for j in range(7) :
                GPIO.output(SEGMENTS[j], NUMBER[i][j])
            time.sleep(0.5)

except :
    GPIO.cleanup()
