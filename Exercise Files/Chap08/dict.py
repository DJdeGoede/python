#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    # or
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr')

    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')
    # or
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
