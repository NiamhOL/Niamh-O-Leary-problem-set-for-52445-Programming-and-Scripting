# Solution to problem 2
# Niamh O'Leary
# ID: G00376339

# Write a program that outputs whether or not today is a day that begins with the letter T.

import datetime


x = datetime.datetime.now()  # using datetime function to identify the current date and time #
print(x.strftime("%A")) # using a string function to print date and time # 

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: # assigning a number to Tues and Thurs, if this number is returned then correct #
    print("Yes- today begins with a T") # if day is equal to 1 or 3 then the dat starts with a T. Therefore print TOday begins with a T #
else:                                       
    print("No - Today does not begin with a T") # otherwise the day does not start with a T and print same #
# for description of method and references please see accompying README file in GITHUB repository # 
