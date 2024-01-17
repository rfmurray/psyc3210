# strings.py  Basics of strings

# we can define a string using single quotes, double quotes, or triple quotes.

s = 'a simple example'  # single quotes

s = "another simple example"  # double quotes

s = """when using triple quotes,
the content of a string
can extend over several lines"""

# we can use indices with strings just like with lists and tuples

s = 'a test string for illustration'

s[0]
s[-1]
s[3:5]
s[-5:]

# strings have many methods available. strings are immutable, so methods
# always return a value, instead of changing the string in place.

s = 'a test string for illustration'

i = s.find('for')  # find the index where a substring begins

i = s.find('xyz')

s = 'jfk,lbj,rmn,grf,jec'
x = s.split(',')   # split a string at a separator; returns a list

t = s.replace(',',':')  # replace all occurrences of a substring
