#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

# MANAGERS = [["Number", "Surname", "Age"],
#              [7274, "Robinson", 37],
#              [7432, "O'Malley", 39],
#              [9824, "Darkes", 38]]

# MANAGERS = [["Number", "Surname", "Age"],
#             [9297, "O'Malley", 56],
#             [7432, "O'Malley", 39],
#             [9824, "Darkes", 38]]

# Totally different
MANAGERS = [["Number", "Surname", "Age"],
             [7214, "Robinson", 37],
             [7412, "O'Malley", 39],
             [9814, "Darkes", 38]]


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


def intersection(table1, table2):
    """
    Established intersection function to perform the intersection set operation on tables 1 and 2. Table 3 variable is
    established to represent the unique rows that appear in both table 1 and table 2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: table3: a table with the header from table1/table2 and unique rows that appear in both tables
    :raises: MismatchedAttributesException:
        if tables table1 and table2 don't have the same attributes
    """
    table3 = []
    i = 0
    j = 0
    if table1[0] != table2[0]:
        return MismatchedAttributesException
    else:
        while i < len(table1):
            while j < len(table2):
                if table1[i] == table2[j]:
                    table3.append(table2[j])
                    j += 1
                else:
                    j += 1
            j = 0
            i += 1

    if len(table3) == 1:
        table3 = None
    return table3

print "Intersection ", intersection(GRADUATES, MANAGERS)


def union(table1, table2):
    """
    Established union function to perform the union set operation on tables 1 and 2. Table 3 variable is
    established to represent the unique rows that appear in either table 1 and table 2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: table3: table1 with unique rows from table2 appended in
    :raises: MismatchedAttributesException:
        if tables table1 and table2 don't have the same attributes
    """
    table3 = []
    j = 1
    if table1[0] != table2[0]:
        return MismatchedAttributesException
    else:
        for i in range(0,len(table1)):
            table3.append(table1[i])
        while j < len(table2):
            if table2[j] not in table1:
                table3.append(table2[j])
            j += 1
        return table3

print "Union ", union(GRADUATES, MANAGERS)


def difference(table1, table2):
    """
    Established intersection function to perform the intersection set operation on tables 1 and 2. Table 3 variable is
    established to represent the unique rows that appear in both table 1 and table 2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: table3: a table with the header from table1/table2 and unique rows from table1 that don't appear in table2
    :raises: MismatchedAttributesException:
        if tables table1 and table2 don't have the same attributes
    """

    if table1[0] != table2[0]:
        return MismatchedAttributesException
    else:
        table3 = [table1[0]]
        i = 1
        while i < len(table1):
            if table1[i] not in table2:
                table3.append(table1[i])
                i += 1
            else:
                i += 1
        if len(table3) == 1:
            table3 = None
        return table3

print "Difference ", difference(GRADUATES, MANAGERS)

#####################
# HELPER FUNCTIONS ##
#####################


def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result