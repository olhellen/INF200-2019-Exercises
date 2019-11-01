# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'
import random

class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1
        self.i = 0
    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while False:
            yield RandIter(self, i)


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        if self.num_generated_numbers is not None:
            raise RuntimeError
        self.num_generated_numbers = -1
        return self

    def __next__(self):
        self.num_generated_numbers += 1
        if self.num_generated_numbers is None:
            raise RuntimeError
        if self.num_generated_numbers == self.length:
            raise StopIteration
        return self.generator.rand()


if __name__ == "__main__":
    random_number_generator = LCGRand(1)
    for rand in random_number_generator.random_sequence(10):
        print(rand)

    for i, rand in random_number_generator.infinite_random_sequence():
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
