#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Python3 program to illustrate
# working of different logical gates

def NOT  (a):    return 'True' if not a else 'False'
def AND  (a, b): return 'True' if a and b else 'False'
def NAND (a, b): return 'True' if not(a and b) else 'False'
def OR   (a, b): return 'True' if a or b else 'False'
def NOR  (a, b): return 'True' if not(a or b) else 'False'
def XOR  (a, b): return 'True' if a !=b  else 'False'
def XNOR (a, b): return 'True' if not(a !=b)  else 'False'       # The XNOR gate (negated XOR) gives an output of 1 both inputs are same and 0 if both are different.

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

