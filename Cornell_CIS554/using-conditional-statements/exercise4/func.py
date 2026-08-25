"""  
A function to search for the first vowel position

Author: Amelia Litvak
Date: 08/08/2025
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)     #  In case there is no 'a'

    if introcs.find_str(s,'a')!=-1:
        result=introcs.find_str(s,'a')
    if introcs.find_str(s,'e',0,result)!=-1:
        #print(s)
        #print(result)
        result=introcs.find_str(s,'e')
    if introcs.find_str(s,'i',0,result)!=-1:
        #print(s)
        #print(result)
        result=introcs.find_str(s,'i')
    if introcs.find_str(s,'o',0,result)!=-1:
        #print(s)
        #print(result)
        result=introcs.find_str(s,'o')
    if introcs.find_str(s,'u',0,result)!=-1:
        #print(s)
        #print(result)
        result=introcs.find_str(s,'u')
    if introcs.find_str(s,'y',1,result)!=-1:
        #print(s)
        #print(result)
        result=introcs.find_str(s,'y',1)

    return -1 if result==len(s) else result

