#!/usr/bin/env python3
from time import sleep
import re
import sys

from espeak import espeak
from espeak import core as espeak_core
from datetime import datetime

from tkinter import Frame, Tk

from randomlyric.randomlyric import get_random_lyric

lyric = get_random_lyric()
lyric = re.sub(r'\( http://.*', '', lyric)

print(lyric)

root = Tk()
app = Frame(master=root)
app.pack()
def callb(event, pos, length):
    print(event)
    # Events can be,
    # WORD, SENTENCE, MARK, PLAY, END, MSG_TERMINATED or PHONEME
    if event == espeak_core.event_MSG_TERMINATED:
        root.quit()
        sys.exit(0)
        print("Quitting")
    if event == espeak_core.event_WORD:
        print("Open Mouth, Close Mouth")

espeak.set_SynthCallback(callb)
t = datetime.now().strftime("%k %M")
#if espeak.synth("Hello, you are talking to Billy Bass. The time is %s"%t):
if espeak.synth(lyric):
    app.mainloop()

root.destroy()
