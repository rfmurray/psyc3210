# practice5b.py  Lecture 5b practice problems

# Some problems will require tools from earlier lectures, such as lists and
# loops. This will be the case in workshop problems from now on.

# 1. Define a function power(x, n) that returns x to the power of n.
# Use it to assign the variable y the value of 2 to the power of 8.

def power(x, n):
    return x ** n

y = power(2, 8)

# 2. Define a function randu(n) that returns a list with n elements,
# where each element is a random number between 0 and 1.

import random

def randu(n):
    x = []
    for i in range(n):
        r = random.uniform(0,1)
        x.append(r)
    return x

# example of using this function
k = randu(10)
print(k)

# 3. Revise your answer to quesiton 2, to define a function randu(n, u, v)
# that returns a list with n elements, where each element is a random
# number between u and v. Give u a default value of 0, and v a default
# value of 1.

def randu(n, u=0, v=1):
    x = []
    for i in range(n):
        r = random.uniform(u,v)
        x.append(r)
    return x

# example of using this function
k = randu(n=10, u=100, v=200)
print(k)

# 3. Create a function bsort(x) that uses the bubblesort algorithm from
# lecture 2b to sort a list x. You can just copy and paste the code from
# lecture 2b into the function.

def bsort(x):
    
    while True:
    
        switched = False
        for i in range(len(x)-1):
        
            if x[i] > x[i+1]:
                tmp = x[i]
                x[i] = x[i+1]
                x[i+1] = tmp
                switched = True
        
        if not switched:
            return

# example of using this function
x = randu(10)  # make an unsorted list of random numbers
bsort(x)       # sort the list
print(x)       # show the sorted list
