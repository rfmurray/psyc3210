# practice2b.py  Lecture 2b workshop problems

# Add code below the following comments, to solve the problems.

# 1. Use a for loop to create a list that contains the squares of the
# integers 0 to 20.

# 2. Repeat problem 1, using a while loop instead of a for loop.

# 3. Is problem 1 or 2 a better way to solve the problem of adding a range
# of integers? Why?

# 4. (a) Use a for loop to make a list of 200 simulated reaction
# times in a perceptual experiment. Make the reaction times normally distributed,
# with a mean of 0.75 and a standard deviation of 0.25. To get these
# random numbers you can use the function random.gauss(). To read the help
# on that function, do this at the command line:
# 
# import random
# help(random.gauss)
# 
# (b) Use a for loop to count the number of reaction times in the list that
# are less than 0.25.
# 
# (c) Use a for loop to count the number of reaction times less than 0.25
# or greater than 1.25.

# 5. Here's a harder problem, if you're up for a challenge.
# 
# Use a for loop to create a list with 100 elements. Each element of the
# list should be a tuple with two elements. The first element of each tuple
# is a random number between 0 and 1. (Use the function random.random() for
# that.) The second element of each tuple is a random number that is greater
# than the first random number but less than 1.
# 
# To figure out how to generate the second random number in the tuple,
# think about the following. If random.random() gives us a number
# between 0 and 1, then what is the range of random numbers that we get
# from these?
#     0.1 + 0.5*random.random()
#     0.5 + 2.0*random.random()
# If you understand this, then you may be able to figure out how to get a
# random number between the first number and 1.
