#!/usr/bin/env python3

from espeak import espeak
from datetime import datetime
from time import sleep
from RPi import GPIO
import os

GPIO.setmode(GPIO.BOARD)
tail_pin = 22
head_pin = 16

GPIO.setup(tail_pin, GPIO.OUT)
GPIO.setup(head_pin, GPIO.OUT)
GPIO.output(tail_pin, False)
GPIO.output(head_pin, False)

t = datetime.now().strftime("%k %M")
#espeak.synth("Hello, you are talking to Billy Bass. The time is %s"%t)
espeak.synth("Here's a little song I wrote, Might want to sing it note for note")

espeak.synth("Don't worry. Be Happy!")

head_state=True
tail_state=False
count=0
while True:
    if count % 3 == 0:
        GPIO.output(tail_pin,tail_state )
        tail_state = not tail_state
    sleep(0.1)
    if count % 1 == 0:
        GPIO.output(head_pin, head_state)
        head_state = not head_state
    count = count + 1
    if count > 1000:
        os.exit(0)

    



