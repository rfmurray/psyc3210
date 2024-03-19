import os, random, imageio, glob
import numpy as np
from psychopy import visual, event, core
import calibrate

# --- part one: load and prepare stimuli ---

# load calibration data
cal = calibrate.CalLum('callum.pkl')

# make list of stimulus image filenames
filenames = glob.glob('images/*.hdr')

# prepare stimuli
stimlist = []
for filename in filenames:
    
    # skip mask files
    if 'mask' in filename:
        continue
    
    # load and calibrate stimulus image
    stimlum = imageio.imread(filename)
    stimlum = stimlum[::-1,:,0]
    stimlum = 75.0 * stimlum
    stimgrey = cal.lum2grey(stimlum)
    stimunit = -1.0 + 2.0*(stimgrey/255.0)
    
    # get mask filename
    base, ext = os.path.splitext(filename)
    maskfilename = base + '_mask' + ext
    
    # load mask image, and find high and low lightness regions
    maskref = imageio.imread(maskfilename)
    maskref = maskref[::-1,:]
    masklow =  maskref[:,:,0]==1
    maskhigh = maskref[:,:,1]==1
    
    # make a list with stimulus information, and append it to the stimulus list
    d = [ filename, stimlum, stimunit, masklow, maskhigh ]
    stimlist.append(d)

# randomize stimulus order
random.seed()
random.shuffle(stimlist)

# --- part two: show stimuli and get match responses ---

# open window and create a few useful objects
win = visual.Window(units='pix', fullscr=True)
im = visual.ImageStim(win)
mouse = event.Mouse(visible=False, newPos=[0,0])
datafile = 'data.csv'

# open data file and write header
fid = open(datafile, 'a')
fid.write('filename,reflum,matchlum\n')

# run trials
for stim in stimlist:
    
    # get information about this stimulus
    filename = stim[0]
    stimlum  = stim[1]
    stimunit = stim[2]
    masklow  = stim[3]
    maskhigh = stim[4]
    
    # get observer's match setting
    while True:
        
        # set match greylevel using mouse position
        limit = 500
        x, y = mouse.getPos()
        matchunit = -1 + (y+limit)/(2*limit)
        matchunit = max(min(matchunit,1),-1)
        
        # show stimulus
        stimunit[maskhigh] = matchunit
        im.image = stimunit
        im.size = stimunit.shape[0:2]
        im.draw()
        win.flip()
        
        # check for keypress responses (return = accept match, q = quit)
        keys = event.getKeys(keyList=['return','q'])
        if len(keys)>0:
            break
    
    # check for quit key
    if keys[0]=='q':
        break
    
    # find luminance of reference and match patches
    reflum = stimlum[masklow].mean()
    matchgrey = 255.0*(matchunit+1.0)/2.0
    matchlum = cal.grey2lum(np.array(matchgrey))
    
    # save data for this trial
    fid.write(f'{filename},{reflum:.2f},{matchlum:.2f}\n')

# close data file and window
fid.close()
win.close()
