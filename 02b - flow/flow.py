# flow.py  Flow control: conditionals and loops

# 1. if-elif-else

x = 3

if x==1:
    print('first case')
    
elif x==2:
    print('second case')
    
elif x==3:
    print('third case')
    
else:
    print('other case')
    print(x)

# can have one 'if' clause, then optional 'elif' clauses (zero or more),
# then optional 'else' clause (zero or one)

# statements with the same level of indentation are grouped together
# under the if, elif, and else clauses. note that you can't mix spaces
# and tabs for indentation.


# boolean expressions

import random
x = random.random()  # generates a random number between 0 and 1
print(x)

if x > 0.1 and x < 0.9:
    print('value is not too extreme')

# logical operators: and, or, not
# 
# arithmetic operators: >, <, >=, <=, ==, !=
# 
# grouping for order of operations: ( )


# 2. for loop

for x in [1, 2, 3]:    # iterate over a list
    print(x)

for x in (1, 2, 3):    # iterate over a tuple
    print(x**2)

for x in range(10):    # iterate over a range of numbers (0...9)
    print(x**3)

# example: find sum of numbers 0 to 99
y = 0
for x in range(100):
    y = y + x

print(y)


# 3. while loop

# get a sample from a limited range of the normal distribution
x = -10
while x < -2 or x > 2:
    x = random.gauss(0,1)

print(x)

# alternative approach, using the break statement; maybe easier to understand
while True:
    x = random.gauss(0,1)
    if x > -2 and x < 2:
        break

print(x)

# we use a for loop when we know how many times we'll need to go through
# the loop. for example, we usually know the number of trials we'll run
# in an experiment.
# 
# we use a while loop when we'll know when we're done with a loop, but
# not necessarily how many runs through the loop it will take. for example,
# a participant in an experiment may press several keys before they press
# a key that is an allowed response.


# 5. an example that uses several topics that we've covered so far: the bubblesort algorithm

# make a list of random numbers
import random
x = []
for i in range(20):
    x.append(random.random())

# show unsorted list
print(x)

# loop indefinitely; we'll use a break statement to exit the while loop
# when we're done sorting the list
while True:
    
    # step through elements of the list x
    switched = False
    for i in range(len(x)-1):
        
        # are these two elements in the wrong order?
        if x[i] > x[i+1]:
            
            # switch order of elements
            tmp = x[i]
            x[i] = x[i+1]
            x[i+1] = tmp
            
            # record that not all elements were in order on this pass
            # through the list
            switched = True
    
    # if we made it through the list without switching any elements,
    # then the list is sorted, and we're done, so exit the while loop
    if not switched:
        break

# show sorted list
print(x)
