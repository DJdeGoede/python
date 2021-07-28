#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]

    game.append('Computer')
    game.remove('Lizard')
    game.insert(0, 'First') # Insert at first position (0), lists are 0-based

    print_list(game)
    x = game.pop(); print(x)
    print_list(game)

    print(', '.join(game))
    print(len(game))

    print(game[0])
    print(game[1:3])

    i = game.index('Spock'); print(i)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
