#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = 5
    print(id(x))
    kitten(x)
    print(f'in main: x is {x}')

def kitten(a):
    print(id(a))
    a = 3
    print('Meow.')
    print(a)

if __name__ == '__main__': main()

 
