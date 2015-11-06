#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Established find function to identify the starting index value of the first instance where a substring appears in
    an input_string
    :param input_string: string
    :param substring: string
    :param start: integer
    :param end: integer
    :return: result: integer
    """
    # Convert the string and substring into lowercase
    input_string = input_string.lower()
    substring = substring.lower()

    # Create initial variables
    i = start

    # Check to see if the substring is within the spliced string
    while i < end:
        if input_string[i:i + len(substring)] == substring:
            return i
            break
        else:
            i += 1
    return -1


def multi_find(input_string, substring, start, end):
    """
    Established multi_find function to identify the starting index value of each instance that a substring appears in
    an input_string
    :param input_string: string
    :param substring: string
    :param start: integer
    :param end: integer
    :return: result: string of all the starting indices where substring is found in input_string
    """
    result = ""
    input_string = input_string.lower()
    substring = substring.lower()
    i = start

    while i < end:
        if input_string[i: i + len(substring)] == substring:
            result = result + str(i) + ","
            i += 1
        else:
            i += 1

    result = result[0:len(result)-1]
    return result
