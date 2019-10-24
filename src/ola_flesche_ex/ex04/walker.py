# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'
import random


class Walker:
    def __init__(self, x0, h):
        self.x0 = x0
        self.h = h
        self.steps = 0

    def move(self):
        self.steps += 1
        step = 2*random.randint(0, 1)-1
        self.x0 = self.x0 + step

    def is_at_home(self):
        if self.x0 == self.h:
            return True

    def walking(self):
        while not self.is_at_home():
            self.move()
        return self.steps

    def get_position(self):
        return self.x0

    def get_steps(self):
        return self.walking()


if __name__ == "__main__":
    print(
        f'\nDistance:   1 -> Path lengths:' 
        f'{sorted([Walker(0,1).get_steps() for step in range(5)])}')
    print(
        f'Distance:   2 -> Path lengths:' 
        f'{sorted([Walker(0, 2).get_steps() for step in range(5)])}')
    print(
        f'Distance:   5 -> Path lengths:' 
        f'{sorted([Walker(0, 5).get_steps() for step in range(5)])}')
    print(
        f'Distance:   10 -> Path lengths:' 
        f'{sorted([Walker(0, 10).get_steps() for step in range(5)])}')
    print(
        f'Distance:   20 -> Path lengths:' 
        f'{sorted([Walker(0, 20).get_steps() for step in range(5)])}')
    print(
        f'Distance:   50 -> Path lengths:' 
        f'{sorted([Walker(0, 50).get_steps() for step in range(5)])}')
    print(
        f'Distance:   100 -> Path lengths:' 
        f'{sorted([Walker(0, 100).get_steps() for step in range(5)])}')
