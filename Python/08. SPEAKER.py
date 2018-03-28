import RPi.GPIO as GPIO
import time

SPEAKER = 25    # BCM. 25(Physical. 22)

C = 261.63      # 도
D = 293.66      # 레
E = 329.63      # 미
F = 349.23      # 파
G = 391.00      # 솔
A = 440.00      # 라

notes = [   # 3차원 배열, [음계, 음표]
    [G, 8], [G, 8], [A, 8], [A, 8], [G, 8], [G, 8], [E, 4],
    [G, 8], [G, 8], [E, 8], [E, 8], [D, 2],
    [G, 8], [G, 8], [A, 8], [A, 8], [G, 8], [G, 8], [E, 4],
    [G, 8], [E, 8], [D, 8], [E, 8], [C, 2]
]

GPIO.setmode(GPIO.BCM)          # BCM 설정
GPIO.setup(SPEAKER, GPIO.OUT)   # BCM. 25 GPIO OUT 설정

pwm = GPIO.PWM(SPEAKER, 0.1)    # PWM(BCM, Frequency)
pwm.start(50)

try :
    for i in notes :                    # notes의 길이만큼 반복
        pwm.ChangeDutyCycle(50)         # 음 출력
        pwm.ChangeFrequency(i[0])       # notes[i]번째 음계를
        time.sleep(4 / i[1] - 0.01)     # notes[i]번째 음표만큼 출력

        pwm.ChangeDutyCycle(0)          # 소리를 끄고
        time.sleep(0.01)                # 0.01초 시간을 둠

except :
    print("error or Pressed [Ctrl-C]")  # 에러가 났거나 [Ctrl - C]를 눌렀을 경우

finally :           # 어찌되었든 끝났을 때
    pwm.stop()      # pwm stop
    GPIO.cleanup()  # GPIO cleanup
    print("end")    # end 메시지 출력
