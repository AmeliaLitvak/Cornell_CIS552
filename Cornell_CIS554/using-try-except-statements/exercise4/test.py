"""  
A test script for the function iso_8601.

Author: Amelia Litvak
Date: 08/11/2025
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')
    result = func.iso_8601('01:01:01')
    introcs.assert_equals(True,result)
    result = func.iso_8601('1:01:01')
    introcs.assert_equals(True,result)
    result = func.iso_8601('1:1:1')
    introcs.assert_equals(False,result)
    result = func.iso_8601('101:1')
    introcs.assert_equals(False,result)
    result = func.iso_8601('01:100:1')
    introcs.assert_equals(False,result)
    result = func.iso_8601('1:10:100')
    introcs.assert_equals(False,result)
    result = func.iso_8601('1,01:01')
    introcs.assert_equals(False,result)
    result = func.iso_8601('1:01:o1')
    introcs.assert_equals(False,result)
    result = func.iso_8601('1tg')
    introcs.assert_equals(False,result)
    result = func.iso_8601('05:-1:01')
    introcs.assert_equals(False,result)
    
    
    # Put your test cases here


if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')