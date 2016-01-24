#!/usr/bin/env python3

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

tail_pin = 22
head_pin = 16

GPIO.setup(tail_pin, GPIO.OUT)
GPIO.setup(head_pin, GPIO.OUT)
GPIO.output(tail_pin, False)
GPIO.output(head_pin, False)

state=True
while True:
    GPIO.output(tail_pin, state)
    sleep(1)
    GPIO.output(head_pin, state)
    sleep(1)
    state = not state

	



