#!/usr/local/bin/python3
"""
Assess part 1, the copied files

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys
import os.path

def check_func1(*files):
    """
    Checks that the files were properly copied over.
    
    Parameter files: The files to check
    Precondition: files is a tuple of string
    """

    if os.path.exists('/home/codio/workspace/exercise8/funcs.py'):
        if os.path.exists('/home/codio/workspace/exercise8/tests.py'):
            result = verifier.grade_first(files[1],0)
        else:
            print("The tests.py file appears to be missing")
            return 1
    else:
        print("The funcs.py file appears to be missing")
        return 1

    
    if not result[0]:
        result = verifier.grade_testcases(files[0],0)
    if not result[0]:
        result = verifier.grade_piggy(files[1],0)
    if not result[0]:
        print("The files are properly copied.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func1('tests.py','funcs.py'))
