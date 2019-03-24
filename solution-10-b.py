# Solution to question 10 #

# Student: Niamh O'Leary #

# ID: G00376339 #

# Write a program that displays a plot of the functions x, x**2 and 2*x in the range [0,4] #

In [1]: import matplotlib.pyplot as plt 

In [2]: import numpy as np

In [3]: x = np.arange(0.0, 4.0, 0.5)  # creates the functions and sets domain lenght #

In [4]: y = x**2

In [5]: dy = 2*x

In [6]: plt.plot(x)  # plot function #
Out[6]: [<matplotlib.lines.Line2D at 0x26ec31be470>]

In [7]: plt.plot(y)
Out[7]: [<matplotlib.lines.Line2D at 0x26ec59b8710>]

In [8]: plt.plot(dy)
Out[8]: [<matplotlib.lines.Line2D at 0x26ec59b7cf8>]

In [9]: plt.title('Question 10 Plots')  # configuring the graph #
Out[9]: Text(0.5, 1.0, 'Question 10 Plots')

In [10]: plt.xlabel('X')
Out[10]: Text(0.5, 0, 'X')

In [11]: plt.ylabel('Y')
Out[11]: Text(0, 0.5, 'Y')

In [12]: plt.show()  # show graph #