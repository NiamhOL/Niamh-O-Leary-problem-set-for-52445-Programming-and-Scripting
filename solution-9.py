# Solution to problem 9 #

# Student: Niamh O'Leary#
# ID: G00376339#

# Write a program that reads the text file moby-dick.txt and outputs every second line.#

In [4]: with open ('moby-dick.txt', 'r') as f:   # first argument is a string to identify the text file. Using 'r' describes the way the file will be used, in this case read only
 
   ...:     for count, line in enumerate(f, start=1):  # enumerate uses two parameters, f the identified text and start(1) which started counting from the first line of text #
   ...:         if count % 2 == 0: # count every second line #
   ...:             print(line)  # print every second line #

   # for description of method and refences please see accompying README file in GITHUB repository #

