#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # method 1 - direct
    kitten('meow', 'grrr', 'purr')
    
    # method 2 - via tuple
    x = ('meow', 'grrr', 'purr')
    kitten(*x)
    
def kitten(*args):
    
        for s in args:
            print(s)
    else: print('No animal sounds given')

if __name__ == '__main__': main()
