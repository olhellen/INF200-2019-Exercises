
def squares_by_comp(*args):
    return [k ** 2 for k in range(*args) if k % 3 == 1]


def squares_by_loop(*args):
    liste = []
    for k in range(*args):
        if k % 3 == 1:
            liste.append(k**2)
    return liste


n = 8
if __name__ == '__main__':
    if squares_by_comp(n) != squares_by_loop(n):
        print('ERROR!')
