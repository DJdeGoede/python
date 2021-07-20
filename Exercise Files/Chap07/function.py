#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import dis

def main():
    x = kitten(11)    # runs the function and implicitly returns None to x
                    # because no return was given in the function
    print(f'{x & 1}')      # 1011 & 0001 = 0001  

    kitten()       # x = None so response will be likewise

    # dis.dis(main)

def kitten(t=1):
    print(f'Meow {t} times.')
    return t

if __name__ == '__main__': main()

 
