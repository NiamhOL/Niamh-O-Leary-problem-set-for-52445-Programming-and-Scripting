# Solution to problem 2
# Niamh O'Leary
# ID: G00376339

# Write a program that outputs whether or not today is a day that begins with the letter T.

import datetime


x = datetime.datetime.now()
print(x.strftime("%A"))

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: 
    print("Yes- today begins with a T")
else:                                       
    print("No - Today does not begin with a T") 

