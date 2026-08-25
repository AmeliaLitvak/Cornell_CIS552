#!/usr/local/bin/python3
"""
Assess part 4, before submission

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func4(*files):
    """
    Checks that the functions are complete and fully tested
    
    Parameter files: The files to check
    Precondition: files is a tuple of string
    """
    result = verifier.grade_docstring(files[0],0)
    if not result[0]:
        result = verifier.grade_docstring(files[1],0)
    if not result[0]:
        result = verifier.grade_first(files[1],0)
    if not result[0]:
        result = verifier.grade_testcases(files[0],0)
    if not result[0]:
        result = verifier.grade_piggy(files[1],0)
    if not result[0]:
        print("The function 'pigify' looks correct and properly tested.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func4('tests.py','funcs.py'))
