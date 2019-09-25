from random import randint as rand

__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'


def dice_number():
    return rand(1, 6) + rand(1, 6)


def your_guess():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def correct_guess(correct_number, guesstry):
    return correct_number == guesstry


if __name__ == '__main__':

    corr_guess = False
    tries = 3
    correct_numb = dice_number()
    while not corr_guess and tries > 0:
        guesses = your_guess()
        corr_guess = correct_guess(correct_numb, guesses)
        if not corr_guess:
            print('Wrong, try again!')
            tries -= 1

    if tries > 0:
        print('You won {} points.'.format(tries))
    else:
        print('You lost. Correct answer: {}.'.format(correct_numb))
