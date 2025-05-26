
import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2


def test_multiplication():
    assert 3 * 4 == 12


def test_division():
    assert 8 / 2 == 4


def test_string_concatenation():
    assert "Hello, " + "world!" == "Hello, world!"


def test_string_length():
    assert len("Python") == 6

def test_list_append():
    my_list = [1, 2, 3]
    my_list.append(4)
    assert my_list == [1, 2, 3, 4]


def test_list_sort():
    my_list = [3, 1, 2]
    my_list.sort()
    assert my_list == [1, 2, 3]


def test_string_split():
    assert "Hello world".split() == ["Hello", "world"]

    
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
