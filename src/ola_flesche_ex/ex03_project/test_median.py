__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_one_element():
    assert median([1]) == 1


def test_odd_number():
    odd_list = [1, 4, 5, 3, 7]
    assert median(odd_list) == 4


def test_even_numbers():
    even_list = [1, 6, 3, 2, 4, 5]
    assert median(even_list) == 3.5



