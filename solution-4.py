# Solution to problem 4#

#Student: Niamh O'Leary#
#ID: G00376339#

def collatz(number):  # The collatz conjecture is that, no matter what number you start with, you will allways reach 1 # 

    if number % 2 ==0: # Even number #
        print(number // 2) # number is even, divide by 2 #
        return number // 2
    
    elif number % 2 == 1:  # if the number is an odd number, 
        result = 3 * number + 1 # multiply by 3 and subtract 1 #
        print(result)
        return result

n = input("Please input a positive number:")  # ask user to input a positive number # 
while n != 1:
     print n = collatz(int(n)) # prints results #


