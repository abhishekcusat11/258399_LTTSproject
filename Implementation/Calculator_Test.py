import pytest
from Implementation import *

TEST_NUM_1 = 3.0
TEST_NUM_2 = 2.0


def test_addition():
    value = addition(TEST_NUM_1, TEST_NUM_2)
    assert value == 5.0


def test_subtraction():
    value = subtraction(TEST_NUM_1, TEST_NUM_2)
    assert value == 1.0


def test_multiplication():
    value = multiplication(TEST_NUM_1, TEST_NUM_2)
    assert value == 6.0


def test_average():
    value = average(TEST_NUM_1, TEST_NUM_2)
    assert value == 2.5
