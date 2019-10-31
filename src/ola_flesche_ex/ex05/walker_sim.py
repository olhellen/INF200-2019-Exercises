# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'
import random


class Walker:
    def __init__(self, start, home):
        self.start = start
        self.home = home
        self.steps = 0

    def move(self):
        self.steps += 1
        step = 2*random.randint(0, 1)-1
        self.start = self.start + step

    def is_at_home(self):
        if self.start == self.home:
            return True

    def walking(self):
        while not self.is_at_home():
            self.move()
        return self.steps

    def get_position(self):
        return self.start

    def get_steps(self):
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        self.seed = seed

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
    a = Simulation(0, 10, 12345)
    print(a.single_walk())

    print(
        f'20 simulation walks from start 0 to home 10 with seed value 12345: '
        f'{[Simulation(0,10,12345).run_simulation(20) for step in range(2)]}')
    print(
        f'20 simulation walks from start 0 to home 10 with seed value 54321: '
        f'{Simulation(0, 10, 54321).run_simulation(20)}\n')
    print(
        f'20 simulation walks from start 10 to home 0 with seed value 12345:'
        f'{[Simulation(10, 0, 12345).run_simulation(20)for step in range(2)]}')
    print(
        f'20 simulation walks from start 10 to home 0 with seed value 54321: '
        f'{Simulation(10, 0, 54321).run_simulation(20)}')
