
# some people find this step necessary on macOS in order for the operating
# system to allow you to download the imageio extension below
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# install an extension to imageio that allows you to read .hdr image files
import imageio
imageio.plugins.freeimage.download()

# install psychopy-minolta and statsmodels modules
import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psychopy-minolta'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'statsmodels'])

