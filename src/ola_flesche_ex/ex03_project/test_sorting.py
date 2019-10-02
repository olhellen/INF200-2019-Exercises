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
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    assert bubble_sort(data)


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    assert bubble_sort(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 2, 5, 1, 2, 9]
    assert bubble_sort(data)


@given(strategies.lists(strategies.integers()))
def test_sorting(list):
    sorted_list = bubble_sort(list)
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
