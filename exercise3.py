#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def schema(table1, table2):
    """
    Created a function to determine first whether the schemas for table 1 and table 2 were the same. It compares
    the length of the first row of both tables and the content of the first row of both tables. Made variables false
     until proven otherwise.
    """

    table_header_1 = table1[0]
    table_header_2 = table2[0]
    result_1 = False
    result_2 = False
    schema_result = False

    length_1 = len(table_header_1)
    length_2 = len(table_header_2)

    if length_1 == length_2:
        result_1 = True

    if table_header_1 == table_header_2:
        result_2 = True

    if result_1 == True and result_2 == True:
        schema_result = True

    return schema_result

# test1 = [["Name","Age","School"],["Robinson",12,"UTS"],["Alice",14,"Bayview Glen"]]
# test2 = [["Name","Age","School"],["James",13,"Hillfield"],["Shauna",20,"Mentor College"]]
#schema(test1, test2)


def union(table1, table2):
    """
    Established union function to perform the union set operation on tables 1 and 2. Table 3 variable is
    established to represent the unique rows that appear in either table 1 and table 2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    table3 = table1
    j = 1
    if schema(table1,table2):
        while j < len(table2):
            if table2[j] not in table1:
                table3.append(table2[j])
            j += 1

    return table3

test1 = [["Name","Age","School"],["Robinson",12,"UTS"],["Alice",14,"Bayview Glen"], ["Shauna",20,"Mentor College"]]
test2 = [["Name","Age","School"],["Robinson",12,"UTS"], ["James",13,"Hillfield"],["Shauna",20,"Mentor College"]]
print union(test1, test2)



def intersection(table1, table2):
    """
    Describe your function

    """
    table3 = [table1[0]]
    i = 1
    j = 1

    if schema(table1,table2):
        while i < len(table1):
            while j < len(table2):
                if table1[i] == table2[j]:
                    table3 = table3 + table2[j]
                    j += 1
                else:
                    j += 1
            i += 1

    return table3

#test1 = [["Name","Age","School"],["Robinson",12,"UTS"],["Alice",14,"Bayview Glen"], ["Shauna",20,"Mentor College"]]
#test2 = [["Name","Age","School"],["Robinson",12,"UTS"], ["James",13,"Hillfield"],["Shauna",20,"Mentor College"]]
#print intersection(test1, test2)


def difference(table1, table2):
    """
    Describe your function

    """
    return []


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


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

