# Solution to problem 4#

#Student: Niamh O'Leary#
#ID: G00376339#

def collatz(number):

    if number % 2 ==0: #Even number#
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Please input a positive number:")
while n != 1:
     print n = collatz(int(n))


