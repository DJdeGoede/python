#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    # or
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr')

    for k in animals.keys(): print (k)
    for v in animals.values(): print (v)
    # print (animals['lion'])

    animals['monkey']='haha'
    print_dict(animals)

    # search for a key
    print('lion' in animals)                                # True
    print('Found!' if 'lion' in animals else 'Not found')    # Alternative text using ternary operator
    print('alpaca' in animals)  # False

    # Be aware:
    # print(animals('godzilla')) gives an error as object does not exist!
    # Use:
    print(animals.get('godzilla'))
    #            ----

def print_dict(o):
    
    " method 1"
    # for x in o: print(f'{x}: {o[x]}')
    
    print('')

    " method 2"
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
