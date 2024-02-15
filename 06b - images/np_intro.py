# np_intro.py  Introduction to the numpy module

from matplotlib import pyplot as plt
from matplotlib import image
import numpy as np  # np is the standard short form for the numpy module

# create an array of zeros
x = np.zeros(shape=(3,4))
x
type(x)

# some important attributes of an array
x.shape     # size of each dimension
x.size      # total number of elements

# more ways of creating arrays

x = np.zeros(shape=(3,4))
x = np.ones(shape=(3,4))

x = np.random.normal(loc=0.0, scale=1.0, size=(3,4))
x = np.random.uniform(low=0.0, high=1.0, size=(3,4))

# arithmetic operations apply to whole arrays

x = np.random.normal(size=(3,4))
y = np.random.normal(size=(3,4))

z = x + y
z = x - y
z = x * y
z = x / y

# load data from a text file
x = np.loadtxt(fname='data.txt', comments='#', skiprows=0, delimiter=',')

# load an image from an image file
im = image.imread('einstein.tif')

# show the image
plt.imshow(im, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.draw()
plt.show()
