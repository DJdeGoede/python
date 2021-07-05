#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = function('Hello')
    print(x)    # Function does its work but does not have a return value
                # In that case the function will return 'None', so x = None

def function(n='no value given'):   # default value if function var is not given
    print(n)

if __name__ == '__main__': main()
