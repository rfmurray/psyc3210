# functions.py  Functions

# abstraction = saying what you will do, without giving the details of exactly
# how you will do it
# 
# - a function is called at some locations in the code, and the implementation
#   is specified elsewhere
# - this approach can make programs easier to write and to understand


# functions

def addit(a, b):
    c = a + b
    return c

addit(10, 20)

# can also do a calculation in the return statement

def addit(a, b):
    return a + b

addit(10, 20)

# can call functions using named arguments; then the order doesn't matter

addit(a=10, b=20)
addit(b=20, a=10)

# can set default values for some or all arguments
# - arguments without default values must come first

def addit(a, b=2):
    return a + b

addit(10)
addit(10,20)
addit(a=10)
addit(a=10,b=20)

# can read variables defined outside the function

x = 1
def addit(a):
    return a + x

# documenting a function: docstrings and help

def addit(a, b=2):
    'returns the sum of two input arguments'
    return a + b

help(addit)

