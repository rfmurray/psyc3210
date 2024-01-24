# experiment1.py  PsychoPy demonstration: mouse tracking

# import modules from psychopy
from psychopy import visual, event
from psychopy.hardware import keyboard

# open a full-screen window
mainwin = visual.Window(size=[], units='pix', fullscr=True)

# create a circle object
stim = visual.Circle(win=mainwin, fillColor='black', radius=25)

# create a mouse object
# - this shouldn't matter, but I've found that if you create the mouse
#   before creating the circle object, the mouse cursor stays visible.
mouse = event.Mouse(visible=False, newPos=[0,0])

# create a keyboard object
kb = keyboard.Keyboard()

# loop indefinitely
while True:

    # get mouse position
    x, y = mouse.getPos()

    # set circle position and draw the circle
    stim.setPos((x,y))
    stim.draw()

    # switch front and back buffers
    mainwin.flip()

    # check for mouse click
    buttons = mouse.getPressed()
    if buttons[0]:
        break

    # check for keypress
    keys = kb.getKeys()
    if 'q' in keys:
        break

# close the window
mainwin.close()
