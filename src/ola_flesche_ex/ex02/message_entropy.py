from collections import Counter
import math


def letter_freq(txt):
    return Counter(txt)


def entropy(message):
    n = len(message)
    message.lower()
    p_i = letter_freq(message)
    for value in p_i:
        p_i[value] = float(p_i[value] / n)
    entrop = 0
    for value in p_i.values():
        entrop += -value * math.log2(value)
    return entrop


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
