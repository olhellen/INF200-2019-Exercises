# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'
from walker_sim import Walker, Simulation

class BoundedWalker(Walker):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(self, start, home, seed, left_limit, right_limit)
        self.start = start
        self.home = home
        self.seed = seed
        self.lef_limit = left_limit
        self.right_limit = right_limit

    def limit(self):



class BoundedSimulation:
   def __init__(self, start, home, seed, left_limit, right_limit):
       super().__init__(self, start, home, seed, left_limit, right_limit)
       self.start = start
       self.home = home
       self.seed = seed
       self.lef_limit = left_limit
       self.right_limit = right_limit

    def limit(self):


