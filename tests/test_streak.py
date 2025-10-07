import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_zeros():
    assert longest_positive_streak([0, 0, 0]) == 0

def test_mixed_numbers_1():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_mixed_numbers_2():
    assert longest_positive_streak([-1, -2, 1, 2, 3, 4, -3, 1, 2]) == 4

def test_streak_at_the_end():
    assert longest_positive_streak([-1, 0, 1, 2, 3]) == 3

def test_streak_at_the_beginning():
    assert longest_positive_streak([1, 2, 3, 0, -1]) == 3

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_negative():
    assert longest_positive_streak([-5]) == 0

def test_single_element_zero():
    assert longest_positive_streak([0]) == 0

def test_long_list():
    assert longest_positive_streak([1] * 100 + [-1] + [1] * 50) == 100