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
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = seed
        self.steps = 0

    def single_walk(self):
        random.seed(self.seed)
        return Walker(self.start, self.home).walking()

    def run_simulation(self, num_walks):
        step_list = []
        random.seed(self.seed)
        for i in range(num_walks):
            step_list.append(Walker(self.start, self.home).walking())
        return step_list


if __name__ == "__main__":
    print(f'{Simulation(0,10,12345).single_walk()}')
    print(f'20 simulation walks from start 0 to home 10 with seed value 12345: '
          f'{[sorted(Simulation(0,10,12345).run_simulation(20)for step in range(2))]}')
