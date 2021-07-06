#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    n = 50
    
    if isprime(n):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')
    
    list_primes(n)

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes(i):
    print(f'Primes up to {i}:', end=' ')
    for n in range(i+1):
        if isprime(n):
            print(n, end=',', flush=True)
    print ('\b ')     # BS to set cursor before last , and then overwrite with a space
    
if __name__ == '__main__': main()



