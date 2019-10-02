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


def test_ordered():
    ord_list = [1, 2, 3, 4]
    assert median(ord_list) == 2.5


def test_reverse_ordere():
    rev_list = [4, 3, 2]
    assert median(rev_list) == 3


def test_value_error():
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    origin_list = [2, 5, 4, 7, 8]
    median_found = median(origin_list)
    assert origin_list == origin_list


def test_tuples():
    tuple = (1, 3, 2, 7, 5)
    assert median(tuple) == 3


