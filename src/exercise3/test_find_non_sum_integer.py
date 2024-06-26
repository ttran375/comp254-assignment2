import pytest

from .find_non_sum_integer import find_non_sum_integer


@pytest.mark.parametrize(
    "A, expected",
    [
        # Edge cases with empty or single-element lists
        ([], None),
        ([0], None),
        ([1], None),
        ([2], None),
        # General cases
        ([1, 2, 3, 4], 9),
        ([5, 7, 1, 2], 15),
        ([0, 1, 2, 3], 7),
        ([10, 20, 30, 40], 81),
        ([2, 2, 2, 2], 5),
        ([3, 5, 8, 13], 27),
        ([1, 1, 1, 1], 3),
        # Edge cases with different ranges and duplicates
        ([4, 6, 8, 10], 21),
        ([15, 16, 17], 35),
        ([100, 200, 300], 601),
        ([9, 12, 15], 31),
        ([99, 100], 201),
        ([25, 35, 45], 91),
        ([7, 7, 7], 15),
        ([6, 3, 6, 3], 13),
        ([5, 5, 5, 5], 11),
        # More diverse ranges and patterns
        ([2, 4, 6, 8, 10], 21),
        ([2, 3, 4, 5], 11),
        ([1, 3, 5, 7, 9], 19),
        ([2, 4, 8, 16], 33),
        ([5, 10, 15, 20], 41),
        ([1, 2, 4, 8], 17),
        ([1, 2, 4, 9], 19),
        ([0, 1, 4, 9], 19),
        ([3, 6, 9, 12], 25),
        ([3, 6, 9, 13], 27),
        ([0, 0, 0, 0], 1),
        ([8, 16, 32, 64], 129),
        # Random sequences and patterns
        ([7, 14, 21], 43),
        ([5, 15, 25, 35], 71),
        ([2, 4, 8, 16, 32], 65),
        ([1, 1, 1, 1, 1, 1], 3),
        ([1, 2, 3, 4, 5, 6], 13),
        ([10, 10, 10, 10], 21),
        ([3, 3, 3, 3], 7),
        ([1, 2, 3, 5, 7, 11], 23),
        ([1, 2, 3, 4, 8], 17),
        ([50, 100, 150], 301),
        ([6, 7, 8, 9], 19),
        ([1, 5, 10, 15, 20], 41),
        ([1, 2, 3, 7, 14], 29),
        ([4, 5, 6, 7], 15),
        ([1, 2, 3, 8, 13], 27),
        ([1, 2, 3, 9, 12], 25),
        ([1, 2, 5, 10, 20], 41),
        ([5, 10, 20, 30, 40], 81),
    ],
)
def test_find_non_sum_integer(A, expected):
    assert find_non_sum_integer(A) == expected
