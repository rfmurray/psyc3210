
import imageio
imageio.plugins.freeimage.download()

import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psychopy-minolta'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'statsmodels'])

