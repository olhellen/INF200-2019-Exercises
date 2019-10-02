import pytest
from inf200_lc import median


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])
