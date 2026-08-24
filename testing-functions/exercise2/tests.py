"""
A test script to test the module funcs.py

Author:Amelia Litvak
Date:06/26/2025
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing
def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    """
    print('Testing has_a_vowel')
    result=funcs.has_a_vowel('aeiou')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('hat')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('let')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('beat')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('been') 
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('wong')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('xxx')
    introcs.assert_equals(False,result)
    result=funcs.has_a_vowel('dajfdohd')
    introcs.assert_equals(True,result)
    result=funcs.has_a_vowel('fly')
    introcs.assert_equals(False,result)
    result=funcs.has_a_vowel('fling')
    introcs.assert_equals(True,result)

def test_has_y_vowel():  
    """
    Test procedure for has_y_vowel
    """
    print('Testing has_y_vowel')
    result=funcs.has_y_vowel('young')
    introcs.assert_equals(False,result)
    result=funcs.has_y_vowel('wheely')
    introcs.assert_equals(True,result)
    result=funcs.has_y_vowel('yoyo')
    introcs.assert_equals(True,result)
    result=funcs.has_y_vowel('hello')
    introcs.assert_equals(False,result)


# Script Code
#print('Testing has_a_vowel')
#print('Testing has_y_vowel')
test_has_a_vowel()
test_has_y_vowel()
print('Module funcs is working correctly')