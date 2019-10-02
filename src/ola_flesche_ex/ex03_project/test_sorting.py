__author__ = 'Ola Flesche Hellenes'
__email__ = 'olhellen@nmbu.no'


from hypothesis import given, strategies


def bubble_sort(tupl):
    lis = list(tupl)
    n = len(lis)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


def test_original_unchanged():
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    data = [1, 2, 3]
    assert bubble_sort(data)


def test_sort_reversed():
    data = [3, 2, 1]
    assert bubble_sort(data)


def test_sort_all_equal():
    data = [1, 2, 5, 1, 2, 9]
    assert bubble_sort(data)


@given(strategies.lists(strategies.integers()))
def test_sorting(int_list):
    sorted_list = bubble_sort(int_list)
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large
