# psychopy_image.py  Show a numpy array as an image in psychopy

# import modules from psychopy
from psychopy import visual
from psychopy.hardware import keyboard
from matplotlib import image
import numpy as np

# open window and keyboard
win = visual.Window(size=[], units='pix', fullscr=True)
kb = keyboard.Keyboard()

# load an image as a numpy array
im = image.imread('einstein.tif')

# flip the image vertically
im = np.flipud(im)

# rescale image so that instead of covering the range 0 to 255,
# it covers the range -1 to 1
im = im/255
im = -1 + 2*im

# create a psychopy image object
imstim = visual.ImageStim(win=win, image=im, size=im.shape)

# show the image
imstim.draw()
win.flip()

# wait for a keypress
kb.waitKeys()

# close the window
win.close()
