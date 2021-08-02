#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    
    # list comprehension
    seq2 = [x * 2 for x in seq]     
    seq3 = [(x, x**2) for x in seq]
    seq4 = [x for x in seq if x % 3 != 0]                    # skip all nrs that can be divided by 3
    seq5 = [x for x in seq if (x & (x-1) == 0) and x != 0]   # only powers of 2

    from math import pi
    seq6 = [round(pi, i) for i in seq]      # round of 
    
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print_list(seq6)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
