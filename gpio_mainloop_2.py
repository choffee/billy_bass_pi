#!/usr/bin/env python3
from time import sleep
import re
import sys

from espeak import espeak
from espeak import core as espeak_core
from datetime import datetime

from randomlyric.randomlyric import get_random_lyric
tail_pin = 22
head_pin = 16
switch_pin = 1
try:
    from RPi import GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(tail_pin, GPIO.OUT)
    GPIO.setup(head_pin, GPIO.OUT)
    GPIO.setup(switch_pin, GPIO.IN)
    GPIO.output(tail_pin, False)
    GPIO.output(head_pin, False)
    on_a_pi = True
except:
    print("Looks like we are not on the Pi, just carrying on anyway")
    on_a_pi = False

import asyncio
loop = asyncio.get_event_loop()


global speaking
speaking=False

def get_lyric():
    lyric = get_random_lyric()
    print(lyric)
    return re.sub(r'\( http://.*', '', lyric)

def open_mouth():
    print("open")
    if on_a_pi:
        GPIO.output(head_pin, True)

def close_mounth():
    print("close")
    if on_a_pi:
        GPIO.output(head_pin, False)

def callb(event, pos, length):
    global speaking
    print(event)
    # Events can be,
    # WORD, SENTENCE, MARK, PLAY, END, MSG_TERMINATED or PHONEME
    if event == espeak_core.event_MSG_TERMINATED:
        print("End of")
        speaking = False

    if event == espeak_core.event_WORD:
        print("Open Mouth, Close Mouth")
        open_mouth()
        sleep(0.1)
        close_mouth()

espeak.set_SynthCallback(callb)

while True:
    espeak.synth(get_lyric())
    speaking=True
    while speaking:
        sleep(1)
        print(".")
    if on_a_pi:
        GPIO.wait_for_edge(switch_pin, GPIO.FALLING)
    else:
        print("Not on a pi so faking a wait")
        sleep(3)
