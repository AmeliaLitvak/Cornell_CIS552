"""
A test script to test the module funcs.py

Author:Amelia Litvak
Date:06/26/2025
"""
import introcs      # For assert_equals
import funcs        # This is what we are testing


# Put your code below this line
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

# Do not write below this line
print('Module funcs is working correctly')
