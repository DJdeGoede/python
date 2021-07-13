#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

def Digits(x=0):
    return(len(str(x))) if True else None

x = 12
print('Nr of digits for {}: {}'.format(x, Digits(x)))

