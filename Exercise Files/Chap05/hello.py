#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Python3 program to illustrate
# working of AND gate
 
def AND (a, b):
 
    if a == 1 and b == 1:
        return 'True'
    else:
        return 'False'
 
# Driver code
if __name__=='__main__': 
 
    print("+-----------------------------------+")
    print("| AND Truth Table      |     Result |")
    print("+----------------------+------------+")
    print(f'| A = False, B = False | {AND(False, False):>10} |')
    print(f'| A = True,  B = False | {AND(True, False):>10} |')
    print(f'| A = False, B = True  | {AND(False, True):>10} |')
    print(f'| A = True,  B = True  | {AND(True, True):>10} |')
    print("+----------------------+------------+")

