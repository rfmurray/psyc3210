# np_more.py  More information about the numpy module

import numpy as np

# transform a sequence into a 1D array
x = np.array([ 1.0, 2.0, 3.0 ])  # transform a list
x = np.array(( 1.0, 2.0, 3.0 ))  # transform a tuple

# transform a sequence of sequences into a 2D array
x = np.array([ [ 1.0, 2.0, 3.0 ], [ 4.0, 5.0, 6.0 ] ])  # list of lists
x = np.array([ ( 1.0, 2.0, 3.0 ), ( 4.0, 5.0, 6.0 ) ])  # list of tuples

# functions apply to whole arrays
u = np.exp(x)
v = np.log(x)
# a few other functions: max, min, mean, median, std, sum, prod, sort

# indexing and slicing

x = np.random.normal(size=(10,5))

# index
y = x[2,3]      # pick a single element: row, column; result is a number, not an array

# slices
y = x[0:5,1]    # multiple rows; result is a 1D array
y = x[:,1]      # all rows; result is a 1D array
y = x[1:3,:]    # multiple rows, all columns; result is a 2D array

x[:,1] = 0      # can also assign new values to parts of an array

# boolean indexing

# define an array
x = np.array([1, 2, 3, 4, 5])

# define a boolean array (same size as x), and use it to select values from x
f = np.array([True, False, False, True, False])
y = x[f]

# define a boolean array using operators on x, and use it to select values from x
f = x > 3
y = x[f]

# same thing, but shortened to a single line
y = x[x>3]

# another example: find perfect squares between 0 and 99
x = np.arange(100)
y = x[ np.round(np.sqrt(x)) == np.sqrt(x) ]

