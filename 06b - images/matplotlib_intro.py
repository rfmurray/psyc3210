# matplotlib_intro.py  Basic plot types and plot formatting

import matplotlib.pyplot as plt

# make up some data
x = [ 1, 2, 3, 4, 5, 6, 7 ]
y = [ 10, 20, 15, 25, 11, 25, 30 ]

# line plots

plt.plot(x, y)
plt.show()

plt.plot(x, y, color='r', marker='o', linestyle='--')
plt.show()

plt.plot(x, y, 'ro--')
plt.show()

# some colours: r g b c m y k w
# some markers: . o v s
# some line styles: - -- -. :
# - see help for plt.plot for others

# bar plot
plt.bar(x=[1,2,3], height=[10,20,15])
plt.xticks(ticks=(1,2,3), labels=['first', 'second', 'third'])
plt.draw()
plt.show()

# formatting: title, axis labels, legend, ticks, text, saving to disk
plt.plot(x, y, color='r', label='duration (minutes)')
plt.title('experimental results')
plt.xlabel('session')
plt.ylabel('duration')
plt.legend(loc='upper right')
plt.xlim(-1,8)
plt.ylim(0,50)
plt.draw()
plt.show()
