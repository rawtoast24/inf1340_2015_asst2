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
    Takes in a string, a substring, and two integers as the start and end points of the first string.
    The function will search letter by letter to see if the substring exists within the start and end points of the
    string.
    If there is a match, the function returns the starting index of the string as an integer. If not, it returns -1

    """
    # Check if the end argument is greater than the start argument
    if end <= start + 1:
        return "Please enter an end argument that is greater than the start argument by at least one."

    # Convert the string and substring into lowercase
    input_string = input_string.lower()
    substring = substring.lower()

    # Create initial variables
    result = 0
    i = start

    # Check if the entered start and end arguments are less than the length of the string
    if start > len(input_string) - 1 or end > len(input_string):
        return "Please enter a start and end integer that is less than the length of the input string."

    # Check to see if the substring is within the spliced string
    while i < end:
        if input_string[i:i + len(substring)] == substring:
            return i
            break
        else:
            i += 1
    return -1

#print find("This is an ex-parrot", "parrot", 0, 20)

def multi_find(input_string, substring, start, end):
    """
    Takes in a string, a substring, and two integers as the start and end points of the input string.
    The function will search letter by letter to see if the substring exists within the start and end points of the
    string.
    The function adds the starting index of each appearance of the substring to a string variable result. If the
    substring does not appear in the input string, result remains empty.
    The function returns the variable result.

    """
    # Create initial variables and convert strings to lowercase
    result = ""
    input_string = input_string.lower()
    substring = substring.lower()
    i = start

# Check if the end argument is greater than the start argument
    if end <= start + 1:
        return "Please enter an end argument that is greater than the start argument by at least one."

    # Check if the entered start and end arguments are less than the length of the string
    if start > len(input_string) - 1 or end > len(input_string):
        return "Please enter a start and end integer that is less than the length of the input string."

    while i < end:
        if input_string[i: i + len(substring)] == substring:
            result = result + str(i) + ","
            i += 1
        else:
            i += 1

    result = result[0:len(result)-1]
    return result

#print multi_find("Ni! Ai! Ni! Ai!", "Ni", 0, 14)

