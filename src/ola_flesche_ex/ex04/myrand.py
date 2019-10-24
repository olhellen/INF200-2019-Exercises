# -*- coding: utf-8 -*-

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2**31-1

    def rand(self):
        while True:
            self.seed = (self.a * self.seed) % self.m
            return self.seed


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers

    def rand(self):
        for number in enumerate(self.numbers):
            if number <= len(self.numbers):
                return
            else:
                raise RuntimeError
