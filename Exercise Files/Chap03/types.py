#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '''
              Hoi
             leuke
            mensjes!    (multiline text)
'''

v1 = 8
v2 = 9

# strings
y  = 'hello there'  # plain text
y1 = y.upper()      # uppercase or .lower() for lowercase
z  = 'This is {} {}'.format('extra', 'stuff')   
a  = '"{0:<10}" and "{1:>10}"'.format('left', 'right')  # alignment
b  = '{1} {0}'.format('1st', '2nd')                     # position swap (start markers with 0)
c  = '"{:<07}" and "{:>07}"'.format(v1, v2)             # alignment #2 (no positional digits with fill up digits)
c1 = f'output: "{v1:<7}" and "{v2:>7}"'                 # using f string (python 3.6 and higher)

# integers
d  = 7 / 3      # normal result (float)
d1 = 7 // 3     # like old Python 2.x - result without remainder (int)
d2 = 7 % 3      # remainder only

q  =  1 > 2    # False
w  =  None

print('{}'.format(x))
print('{}'.format(y))
print('{}'.format(y1))
print('{}'.format(z))     # text within text
print('{}'.format(a))
print('{}'.format(b))
print('{}'.format(c))
print('{}'.format(c1))
print('{}'.format(q))

print('Type of q = {}'.format(type(q)))            # which type?
print('Type of w = {}'.format(type(w)))

print('result of 7/3 = {}'.format(d))
print('int result of 7/3 = {}'.format(d1))
print('remainder of 7/3 = {}'.format(d2))

print()
# sequences
x = (1,'two',3.0, [4, 'four'],5)
print('x is {}'.format(x))
print(type(x))



