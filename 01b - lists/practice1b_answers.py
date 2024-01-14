# practice1b_answers.py  Answers to practice exercises for lecture 1b

# 1. Create a list x that contains the numbers 100 to 110.
x = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# 2. Set a variable y equal to the following elements or sublists of x. When
# possible, write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 11.

# 2a. the first element of x
y = x[0]

# 2b. the first five elements of x
y = x[:5]

# 2c. the last element of x
y = x[-1]

# 2d. the last five elements of x
y = x[-5:]

# 2e. the first three elements of x and the last three elements of x
y = x[:3] + x[-3:]

# 2f. the first five elements of x, repeated ten times, i.e., the list
#     [ 100, ..., 104 ], repeated ten times
y = 10 * x[:5]

# 2g. the largest element of x, repeated five times
y = 5 * [ max(x) ]

# 2h. the smallest element of x, repeated a number of times equal to
#     the largest element of x
y = max(x) * [ min(x) ]

# 3. Change the list x as follows.

# 3a. set the first element to zero
x[0] = 0

# 3b. set the last three elements to zero
x[-3:] = 3 * [0]

# 3c. delete the fourth and fifth elements of x
del x[3:5]

# 3d. delete the last element of x
del x[-1]

# 3e. append the value 120 to the end of x
x.append(120)

# 3f. append the first three elements of x to the end of x
x.extend(x[0:3])

# 3g. sort the elements of x
x.sort()

# 4. Create a tuple z that contains the following elements.

# 4a. the number 50
z = (50,)

# 4b. the number 50, repeated three times
z = 3 * (50,)

# 4c. the numbers 1, 2, and 3, in that order, repeated five times
z = 5 * ( 1, 2, 3 )
