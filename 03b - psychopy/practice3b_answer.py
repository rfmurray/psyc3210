# practice3b_solution.py  Solution to practice problem for lecture 3b

import math, random
from psychopy import visual, event

# open window
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create circle objects
circle1 = visual.Circle(win, fillColor='white', lineColor=None, radius=250)
circle2 = visual.Circle(win, fillColor='black', lineColor=None, radius=25)

# create mouse object
mouse = event.Mouse(visible=False)
mouse.setPos([ random.randint(-250,250) for i in range(2) ])

# loop indefinitely
while True:

    # get mouse position
    x, y = mouse.getPos()
    
    # draw outer circle
    circle1.draw()
    
    # position and draw inner circle
    circle2.setPos((x,y))
    circle2.draw()
    win.flip()

    # check for mouse click
    if mouse.getPressed()[0]:
        break

# close the full-screen window
win.close()
