"""
The test script for the course project.
Author:Amelia Litvak
Date:07/07/2025
"""
import introcs
import funcs
def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')
    result=funcs.matching_parens('(X) Y Z')
    introcs.assert_equals(True,result)
    result=funcs.matching_parens('(()) 1 2')
    introcs.assert_equals(True,result)
    result=funcs.matching_parens('()')
    introcs.assert_equals(True,result)
    result=funcs.matching_parens('A )B( C')
    introcs.assert_equals(False,result)
    result=funcs.matching_parens('')
    introcs.assert_equals(False,result)
    result=funcs.matching_parens('((')
    introcs.assert_equals(False,result)
    result=funcs.matching_parens('rggn')
    introcs.assert_equals(False,result)
    result=funcs.matching_parens('(A)(S)(D)')
    introcs.assert_equals(True,result)


    


def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')
    result=funcs.first_in_parens('(X) Y Z')
    introcs.assert_equals('X',result)
    result=funcs.first_in_parens('(() 1 2 ')
    introcs.assert_equals('(',result)
    result=funcs.first_in_parens('(A A) (B) C')
    introcs.assert_equals('A A',result)
    result=funcs.first_in_parens('(X(Q) (Y) (Z)')
    introcs.assert_equals('X(Q',result)
    result=funcs.first_in_parens(')))(1(2(3(4XXXXXXXXXX))))')
    introcs.assert_equals('1(2(3(4XXXXXXXXXX',result)
    

# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')