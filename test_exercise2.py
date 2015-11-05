#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("This is an ex-parrot", "flamingo",0,20) == -1


def test_find_out_of_string():
    assert find("This is an ex-parrot", "parrot", 21, 20) == -1
    assert find("This is an ex-parrot", "parrot", 0, 25) == 14


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"


def test_find_more():
    """
    Establish other function to test more scenarios of find_basic
    """

    assert find("This is an ex-parrot", "parrot", 0, 25) == 14
    assert find("This is an ex-parrot", "parrot", 16, -5) == -1
    assert find("This is an 3x-parrot", "parrot", 0, 20) == 14
    assert find(" T his i s an par rot", "parrot", 0, 20) == -1


def test_multi_find_more():
    """
    Establish other function to test more scenarios of find_multi
    """

    assert multi_find("Ni! Ni! Ni! Ni!", "Ni!", 2, 19) == "4,8,12"
    assert multi_find("Ni! nI! ni! NI!", "Ni!", 0, 15) == "0,4,8,12"
    assert multi_find("Ni!!!!! Ni! Ni! Ni!", "Ni", 0, -1) == ""
    assert multi_find("Ni ! Ni! Ni! Ni!!", "Ni", 9, -9) == ""
    assert multi_find("Ni!  N!! Ni!Ni!", "Ni", 0, 15) == "0,9,12"
