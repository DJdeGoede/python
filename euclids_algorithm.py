#!/usr/bin/env python3
" Euclids algorithm: find greatest divisor of two numbers "

def euclid (*args):
    if len(args) != 2:
        print (f'[!] Need two numbers, {len(args)} number(s) given.')
        return

    m = args[0]; n = args[1]
    if args[0] < args[1]:           
        m = args[1]; n = args[0]
    
    # save original values
    a = m
    b = n    
    
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r
    print(f'[v] Greatest common divisor of {a} and {b} = {n}')

def main():
    euclid(40,56)

if __name__ == '__main__':
    main()



