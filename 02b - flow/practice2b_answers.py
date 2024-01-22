# practice2b_answers.py  Answers to practice exercises for lecture 2b

# 1. Use a for loop to create a list that contains the squares of the
# integers 0 to 20.

x = []
for i in range(21):
    x.append(i**2)

# 2. Repeat problem 1, using a while loop instead of a for loop.

x = []
i = 0
while i<=20:
    x.append(i**2)
    i += 1

# 3. Is problem 1 or 2 a better way to solve the problem of adding a range
# of integers? Why?

# The for loop is better, as the code is simpler and easier to understand.
# For loops are usually preferable when we know how many times we'll need
# to go through the loop, as we do here.

# 4. (a) Use a for loop to make a list of 200 simulated reaction
# times in a perceptual experiment. Make the reaction times normally distributed,
# with a mean of 0.75 and a standard deviation of 0.25.

import random

rt = []
for i in range(200):
    rt.append(random.gauss(0.75,0.25))

# (b) Use a for loop to count the number of reaction times in the list that
# are less than 0.25.

n = 0
for x in rt:
    if x < 0.25:
        n = n + 1

# (c) Use a for loop to count the number of reaction times less than 0.25
# or greater than 1.25.

n = 0
for x in rt:
    if x < 0.25 or x > 1.25:
        n = n + 1

# 5. Use a for loop to create a list with 100 elements. Each element of the
# list should be a tuple with two elements. The first element of each tuple
# is a random number between 0 and 1. (Use the function random.random() for
# that.) The second element of each tuple is a random number that is greater
# than the first random number but less than 1.

import random

x = []
for i in range(100):
    u = random.random()
    v = u + (1-u)*random.random()
    x.append((u,v))
