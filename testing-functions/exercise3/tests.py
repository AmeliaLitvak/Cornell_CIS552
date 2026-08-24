"""
A test script to test the module func.py

Author:Amelia Litvak
Date:07/01/2025
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')
    
    # Put your tests below this line
    result=funcs.replace_first('crane','a','o')
    introcs.assert_equals('crone',result)
    result=funcs.replace_first('poll','l','o')
    introcs.assert_equals('pool',result)
    result=funcs.replace_first('crane','cr','b')
    introcs.assert_equals('bane',result)
    result=funcs.replace_first('hello','e','a')
    introcs.assert_equals('hallo',result)
    result=funcs.replace_first('HELLO','E','e')
    introcs.assert_equals('HeLLO',result)
    result=funcs.replace_first('$$$123','$$$1','3')
    introcs.assert_equals('323',result)
    result=funcs.replace_first('hello','he','ba')
    introcs.assert_equals('ballo',result)
    result=funcs.replace_first('aaaa','a','bb')
    introcs.assert_equals('bbaaa',result)
    result=funcs.replace_first('a','a','')
    introcs.assert_equals('',result)

    
# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')
