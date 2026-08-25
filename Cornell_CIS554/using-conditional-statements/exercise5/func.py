"""  
A function to check the validity of a numerical string

Author: Amelia Litvak
Date: 08/08/2025
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.
    
    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.
    
    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).
    
    Examples: 
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False
    
    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    length=len(s)
    if length==1 and introcs.isdigit(s)==True:
        return True
    elif length>1 and length<=3 and introcs.isdigit(s)==True and s[0]!='0':
        return True
    elif length>3 and length<=7:
        substring1=s[0:-4]
        substring2=s[-4]
        substring3=s[-3:]
        #print(s, substring1, substring2, substring3)
        if introcs.isdigit(substring1)==True and introcs.isdigit(substring3)==True and substring2==',' and s[0]!='0':
            return True
        else:
            return False
    else:
        return False
    

