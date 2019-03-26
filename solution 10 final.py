# Solution to question 10 #

# Student: Niamh O'Leary #

# ID: G00376339 #

# Write a program that displays a plot of the functions x, x**2 and 2*x in the range [0,4] #

import matplotlib.pyplot as plt  # import matplotlib #

import numpy as np # import numpty #

x = np.arange(0.0, 4.5, 0.5) # values for x are between 0 and 4.5 in increments of 0.5 #

y = x # assigning a variable name for x #

y2 = x**2  # assigning a variable name for x**2 #

y3 = 2*x # assigning a variable name for 2*x #

plt.plot(x, y, '-b', label = 'x')  # customising and labeling line to denote x #

plt.plot(x, y2, '-r', label = '$x**2$') # customising and labeling line to denote x**2 # 

plt.plot(x, y3, '-g', label = '$2*x$') # customising and labelling line to denote 2*x #

plt.legend(loc='upper left', fontsize=16) # adding and positioning a legend '

plt.title('Problem 10: function of x plots', fontsize=18)  # assigning a graph title and font size # 

plt.show()  # show the plot # 

# for description of metthod and references, please see accompying README file in GITHUB repository #



