#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

    print_set(a | b)    # a or b
    print_set(a & b)    # a and b
    print_set(a ^ b)    # xor (a or b but not both)
    print_set(a - b)    # in a not in b
    print_set(b - a)    # in b not in a

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
