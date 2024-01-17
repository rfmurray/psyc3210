# dictionaries.py  Basics of dictionaries

# 1. creating a dictionary

expt = {'subject' : 'jfk', 'time' : '14-Jan-1960 16:00', 'condition' : 'validcue'}

# 2. basic dictionary operations

expt['subject']          # get entry corresponding to key 'subject'
expt['subject'] = 'lbj'  # assign entry corresponding to key 'subject'
expt['rt'] = 0.145       # key doesn't have to already exist

del expt['rt']           # delete entry corresponding to key 'rt'
expt['rt']               # error ("raises an exception"; KeyError)

