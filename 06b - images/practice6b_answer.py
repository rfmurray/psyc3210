# practice6b_answer.py

# import modules from psychopy
from psychopy import visual, core
from psychopy.hardware import keyboard
from matplotlib import image
import numpy as np

# open window and keyboard
win = visual.Window(fullscr=True, units='pix', waitBlanking=True)
kb = keyboard.Keyboard()

# create a psychopy image object
imstim = visual.ImageStim(win=win, size=(256,256))

while True:
    
    # create the image
    im = np.random.uniform(low=-1.0, high=1.0, size=(256,256))
    imstim.image = im
    
    # show the image
    imstim.draw()
    win.flip()
    
    # quit after keypress
    if kb.getKeys():
        break

# close the window
win.close()
