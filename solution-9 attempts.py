
In [6]: cd .
C:\Users\Niamh\Desktop

In [7]: f = open('moby-dick.txt', 'r')

In [8]: for line in f.read().spli('\n)[::2]:
   ...:     print(line)
  File "<ipython-input-8-51f3add23712>", line 1
    for line in f.read().spli('\n)[::2]:
                                        ^
SyntaxError: EOL while scanning string literal


In [9]: cd .
C:\Users\Niamh\Desktop

In [10]: step = 2

In [11]: with open('moby-dick') as handle:
    ...:     for lineno , line in enumerate(handle):
    ...:         if lineno % step == 0:
    ...:             print(line)