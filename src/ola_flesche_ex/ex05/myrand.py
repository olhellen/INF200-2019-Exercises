# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1

    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed

class RandIter(LCGRand):
    def __init__(self, random_number_generator, length):
        super().__init__(self.seed)
        self.generator = LCGRand()
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):

        pass

    def __next__(self):

    def infinite_random_sequence(self):

        pass