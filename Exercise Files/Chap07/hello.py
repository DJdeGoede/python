#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1(f):
    def f2():
        print('Before')
        f()         # this runs f3, because f = f3 here
        print('After')
    return f2

@f1         # decorator (same as f3 = f1(f3) )
def f3():
    print('Code in between')

f3()


