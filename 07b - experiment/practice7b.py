# practice7b.py  Lecture 7b practice problem

# 1. The experiment covered in the lecture saves the filename of the
# stimulus image on each trial. Instead, we may want to save just the
# name of the illusion, which is part of the filename. For example,
# if the filename is 'images/rgb_simcon.hdr', then we may wish to extract
# the illusion name 'simcon' (which is short for simultaneous contrast)
# from this filename, and save that in the data file instead.
# 
# Read about the functions os.path.split() and os.path.splitext() to learn
# how to extract the path, base filename, and extension from a string
# that is a full filename. Also read about the split() method of strings,
# which allows you to break a string up into parts. Use these tools
# to extract the illusion name from the filename. Then modify the experiment
# so that instead of writing the full filename to the data file, just this
# shorter name is written to the datafile instead.
