#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Takes in a string argument and returns it in Pig-Latin
    If the entered string begins with a vowel, append 'yay' to the end of the string
    Otherwise, move all letters up till the first vowel from the entered string to the back and append 'ay' to the end
    """
    result = ""

    word = word.lower()

    if word.isalpha() == False:
        return "Please only enter alphabetic characters, and please enter at least one."

    elif word[0] in ("a","e","i","o","u"):
        result = word + "yay"
    else:
        while word[0] not in ("a","e","i","o","u"):
            word = word[1:] + word[0]
            result = word + "ay"
    return result

# pig_latinify("scram")

