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
    word = raw_input("enter the word you wish to translate to Pig-Latin")
    

    return result