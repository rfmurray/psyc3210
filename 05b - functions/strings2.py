# strings2.py  More strings

# there are several ways of embedding the values of variables in strings.
# the newest, best, and easiest is probably f-strings, which have been available
# from python 3.6 onwards.

height = 8.41315934
volume = 30.4193

s = f'the height is {height} cm and the volume is {volume} cm^3'

# we can also specify the format of the variable in the string.

s = f'the height is {height:.2f} cm and the volume is {volume:.2f} cm^3'

# the embedded format codes work like this:
# 
#     {[variable name]:[width].[decimals][data type]}
# 
# width = how many spaces the value should take up (at a minimum)
# decimals = number of decimal places (not allowed for int and string; see next line)
# data type = f for float, d for int, s for string

# for example, we can make a string containing floating point numbers with
# two decimal places, and make sure that each number takes up at least ten
# characters, so that they line up as columns in a table with many such strings.

s = f'{height:10.2f},{volume:10.2f}'

