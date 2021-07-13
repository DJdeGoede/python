#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quaaack!'
    
    def express(self):
        print(self.sound)

    def move(self):
        print('Waggles like a creature.')

class Human:
    sound = 'Hi I am a human beeing!'
    
    def express(self):
        print(self.sound)

    def move(self):
        print('Walks like a two-legged madman.')
        
def main():
    donald = Duck()
    donald.express()
    donald.move()

    dick   = Human()
    dick.express()
    dick.move()
    


if __name__ == '__main__': main()
