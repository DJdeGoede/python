#!/usr/bin/env python3

# without money precision
x = .1 + .1 + .1 - .3
print(f'x is {x}')
print(type(x),'\n')

# with money precision
#    always use this when working with money to avoid minor floating differences
from decimal import *
a = Decimal('.10')      # use 2 digits for 2 digit end result
b = Decimal('.30')
x = a + a + a - b
print(f'x is {x}')
print(type(x))

