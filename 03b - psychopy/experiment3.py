# experiment3.py  PsychoPy demonstration: orientation discrimination, with additional features

import random
from psychopy import visual, event, core, sound

# set stimulus properties
anglelist = [0.25, 0.5, 1, 2, 4, 8]  # list of grating angles (degrees)
wavelength = 40.0           # sine wave wavelength (pixels)
stimsize = 250.0            # stimulus size (pixels)
stimdur = 0.5               # stimulus duration (seconds)
bgcolor = (0,0,0)           # background colour (range is -1 to 1)

# open a full-screen window
win = visual.Window(size=[], units='pix', color=bgcolor, waitBlanking=True, fullscr=True)
win.mouseVisible = False

# create a sine wave grating object
grating = visual.GratingStim(win=win, mask='gauss', size=stimsize, pos=[0,0], sf=1/wavelength)

# create sound objects
lowbeep = sound.Sound(value='C',  octave=4, secs=0.1, volume=0.8)
highbeep = sound.Sound(value='C', octave=5, secs=0.1, volume=0.3)

# open data file
f = open('data.txt', 'a')

# run trials
for t in range(100):

    # choose grating orientation
    angle = random.choice(anglelist)
    stimright = random.choice([True, False])
    if stimright==False:
        angle = -angle

    # show grating
    grating.ori = angle
    grating.draw()
    win.flip()
    core.wait(stimdur)
    win.flip()

    # wait for a keypress response
    keys = event.waitKeys(keyList=['lshift', 'rshift', 'q'])
    if keys[0]=='q':
        break
    
    # process the response
    respright = keys[0]=='rshift'
    correct = respright==stimright
    
    # give auditory feedback
    if correct:
        highbeep.seek(0)        # rewind to beginning of sound
        highbeep.play()         # play the sound
    else:
        lowbeep.seek(0)
        lowbeep.play()

    # write trial information to data file
    trialdata = f'{t+1:d},{angle:f},{stimright:d},{respright:d},{correct:d}\n'
    f.write(trialdata)

    # pause before next trial
    core.wait(0.5)

# close the full-screen window
win.close()

# close the data file
f.close()
