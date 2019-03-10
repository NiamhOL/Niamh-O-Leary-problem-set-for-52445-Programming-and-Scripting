# Solution to probem 5 #

# Student: Niamh O'Leary
# ID: G00376339 #

# Write a problem that asks the user to input a postive integer and tells the user whether or not the number is a prime #

# take an input from the user
 num = int(input("Please enter a positive integer:"))

 if num > 1: # prime numbers are greater than 1#
     for i in range(2,num): #this checks if the number is divisible by any number from 2 to -1#
         if (num % i) == 0: #if the number divided by i repeating leaves a remainder#
             print(num, "This is not a prime number") #cannot be a prime number. Tell user this#
             print(i, "times", num//i, "is", num) #A composite number must have a factor less then the square root of that number, otherwise the number is a prime number#
             break
        else:
            print(num, "This is a prime number") #it is a prime number. Tell user this#

else:
    print(num, "This is not a prime number") # if the input number is less than or equal to 1, it is not a prime number# 
