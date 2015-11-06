#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

ALUMNI = [["Number", "Surname", "Age"],
          [7274, "Robinson", 37],
          [7432, "O'Malley", 39],
          [9824, "Darkes", 38]]

ACTORS = [["Number", "Surname", "Age"],
          [5400, "Bernard", 40],
          [7302, "Markham", 34],
          [8776, "Shingle", 52]]

#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################
def test_intersection():
    """
    Test intersection operation. If both tables are the same, function should return a new table
     that contains all the unique rows that appear in both tables.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"],
              [[7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]
    assert is_equal(result, intersection(GRADUATES, ALUMNI))

def test_union():
    """
    Test union operation. If both tables have the same schema the function will return a new table that contains all
    unique rows that appear in either table. Tested three comparisons, one where two tables were semi-similar, one where
    they were the same and one where they were completely different.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, ALUMNI))

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [5400, "Bernard", 40],
              [7302, "Markham", 34],
              [8776, "Shingle", 52]]

    assert is_equal(result, union(GRADUATES, ACTORS))


def test_difference():
    """
    Test difference operation. After its been determined that the schema of both tables is the same the
    function will return a new table that holds all unique rows that appear in the first table but not the second.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))


def test_schemas():
    """
    Established a function to test whether the schemas of both tables are the same. If they are not the program
    raises a MismatchedAttributesException error.
    """
