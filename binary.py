#!/usr/bin/env python3
" binary tricks "

# functions
def binary(n): return f'{n:b}'
def powerof2(n): return True if (n & (n-1) == 0) and n != 0 else False

# set a binary direct:  x = 0b110101 (53)

# A different way of calculating powers of 2
print('Powers of 2:')
for i in range(256): 
    if powerof2(i): print (i, end=' ')
print ('\n')

# dec to bin
d = 157
print(d, 'is', binary(d), 'in binary')

# bin to dec
b = 0b110101
print(bin(b), 'is', b, 'in decimal')    # b is actually stored as int(dec) value
                                        # to print the binary value you need to 
                                        # convert the int to binary

  
# Printing the log base 2 of 14
# to have x possible values, calculate 2log(x)

import math

x = 16
print ('Logarithm base 2 of',x,'is :', math.log2(x))
print ('You need', math.ceil(math.log2(x)),'bits to store',x,'values.')


