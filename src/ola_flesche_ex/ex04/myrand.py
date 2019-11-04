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
        self.number = 0
        self.counts = -1

    def rand(self):
        if self.counts == len(self.numbers)-1:
            raise RuntimeError
        else:
            self.counts += 1
            num = self.numbers[self.counts]
        return num


if __name__ == "__main__":
    lcg = LCGRand(67)
    lis = ListRand([4, 7, 9, 3, 40])
    print(f'\nA few random numbers generated from LCGRand with 67 as seed:' f'{[lcg.rand(), lcg.rand(), lcg.rand()]}')
    print(f'Numbers generated from the ListRand class:' f'{[(lis.rand()), (lis.rand()), lis.rand(), lis.rand(), lis.rand()]}')
