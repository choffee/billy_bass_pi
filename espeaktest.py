#!/usr/bin/env python3

from espeak import espeak
from datetime import datetime
from time import sleep

t = datetime.now().strftime("%k %M")
espeak.synth("Hello, you are talking to Billy Bass. The time is %s"%t)

sleep(3)
