# lists.py  Lists and tuples

# 1. Variables and basic mathematical operations

x = 3.0
y = 4.0

z = x + y
z = x - y
z = x * y
z = x / y
z = x ** y
z = ( x + y ) * y

# mathematical functions

import math

z = math.sin(x)
z = math.log(x)
z = math.exp(x)
z = math.pi

# 2. Data types

# float
x = 3.1415
type(x)
y = 0.0
type(y)

# int
y = 0
type(y)

# bool
x = True
type(x)
y = False
type(y)

# 3. Lists

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # a list
type(x)

# many of our examples will be lists of numbers, but lists can contain
# any data type, including other lists
y = [0, 0.0, True, [10,20,30]]
type(y)

# - index

x[0]   # elements are numbered starting at zero
x[1]
x[4]
x[20]  # error

# - slice

x[0:3]  # first index is inclusive, second is exclusive
x[2:4]

# omitted indices default to beginning or end of list
x[:3]
x[5:]
x[:]

# negative indices count back from end of list
x[-1]
x[-5]
x[4:-3]
x[-3:-1]
x[-3:0]  # result is an empty list when first index is after second index
x[-3:]
x[:-4]

# we can assign the results of any of the above operations to a new variable
y = x[:-4]

# - addition and multiplication

a = [10, 20, 30] + [40, 50, 60]  # concatenates lists
b = 3 * [10, 20, 30]             # repeats a list

# - length, minimum, maximum, sum

len(x)
min(x)
max(x)
sum(x)

# mean
m = sum(x)/len(x)

# - item assignment

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

x[1] = 50
x[20] = 50  # error; can't assign to a position that doesn't already exist

# - assigning to slices

x[0:3] = [100, 200, 300]
x[0:3] = [100, 200, 300, 400, 500]  # can change number of elements

# - deleting elements and slices

del x[3]
del x[3:5]

# - list methods

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# adding elements
x.append(110)                # appends value; changes x in place
x.extend([1000, 2000, 3000]) # appends multiple values

# reordering elements
x.sort()        # sorts list in place
y = sorted(x)   # returns a sorted copy of x, and leaves x unchanged

# as mentioned above, lists can contain any data type
y = [0, 0.0, True, [10,20,30]]
len(y)
type(y[0])
type(y[3])

# 4. Tuples

# - lists are mutable; you can change their contents
# - tuples are immutable

x = (10, 20, 30)
x = 10, 20, 30      # for tuples, the parentheses are optional
type(x)

# we can use many operations from lists on tuples too

x[1]                # index
x[1:3]              # slice
x + x               # concatenate
3*x                 # repeat
len(x)              # length
max(x)              # maximum

# but we can't do anything that would change a tuple

del x[0]            # error
x[0] = 100          # error
x.append(50)        # error
