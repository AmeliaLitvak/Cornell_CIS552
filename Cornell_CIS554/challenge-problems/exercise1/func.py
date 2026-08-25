"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Amelia Litvak
Date: 08/15/2025
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.
    
    If sub does not appears anywhere in text, this function returns the empty tuple ().
    
    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)
    
    Parameter text: The text to search
    Precondition: text is a string
    
    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    result=()
    for value in range(0,len(text)):
        index1=introcs.find_str(text,sub,value)
        if index1 in result:
            pass
        elif index1 >= 0:
            result= result+(index1,)
        #print(result)
    return result
