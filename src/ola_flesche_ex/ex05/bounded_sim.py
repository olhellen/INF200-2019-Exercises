# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'
from src.ola_flesche_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def limit(self):
        while not super().is_at_home():
            super().move()
            if self.start < self.left_limit:
                self.start = self.left_limit
                self.steps -= 1
            elif self.start > self.right_limit:
                self.start = self.right_limit
                self.steps -= 1
        return super().get_steps()


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def limit_sim(self):
        sim_walker = BoundedWalker(self.start, self.home, self.left_limit,
                                   self.right_limit)
        n = 0
        while not sim_walker.is_at_home():
            sim_walker.move()
            n += 1
        return n


if __name__ == "__main__":
    print(f'{[BoundedWalker(0, 20, 0, 20).limit() for _ in range(20)]}')
    print(f'{[BoundedWalker(0, 20, -10, 20).limit() for _ in range(20)]}')
    print(f'{[BoundedSimulation(0, 20, 12, 0, 20).limit_sim()for _ in range(20)]}')
    print(f'{BoundedSimulation(0, 20, 12, -10, 20).limit_sim()}')
    print(f'{BoundedSimulation(0, 20, 12, -100, 20).limit_sim()}')
    print(f'{BoundedSimulation(0, 20, 12, -1000, 20).limit_sim()}')
