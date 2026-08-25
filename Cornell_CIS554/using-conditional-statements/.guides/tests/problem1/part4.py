#!/usr/local/bin/python3
"""
Assess part 4, all remaining vowels

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func4(file):
    """
    Checks that the function works all vowels
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_func(file,3)
    if not result[0]:
        print("The function appears to work for all vowels.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func4('func.py'))
