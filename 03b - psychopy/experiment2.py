# experiment2.py  PsychoPy demonstration: orientation discrimination

import random
from psychopy import visual, event, core
from psychopy.hardware import keyboard

# open a full-screen window
win = visual.Window(size=[], units='pix', fullscr=True)

# create a sine wave grating object
grating = visual.GratingStim(win=win, size=250, mask='gauss', sf=0.05)

# create mouse and keyboard objects
mouse = event.Mouse(visible=False)
kb = keyboard.Keyboard()

# run trials
for t in range(100):

    # assign the grating a random orientation between -10 and 10 degrees
    # (0 degrees is vertical)
    angle = random.uniform(-10,10)
    grating.ori = angle
    
    # show the grating for 0.5 seconds
    grating.draw()
    win.flip()
    core.wait(0.5)
    win.flip()

    # wait for a keypress response
    keys = kb.waitKeys(keyList = ['lshift', 'rshift', 'q'])
    if 'q' in keys:
        break

    # pause before next trial
    core.wait(0.5)

# close the full-screen window
win.close()
