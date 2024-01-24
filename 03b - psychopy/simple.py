# simple.py

from psychopy import visual, core

# open a window
mainwin = visual.Window(size=[800, 600], units='pix')

# create and draw a circle object
stim = visual.Circle(win=mainwin, fillColor='black', radius=25)
stim.draw()

# switch front and back buffers
mainwin.flip()

# pause
core.wait(1)

# close the window
mainwin.close()
