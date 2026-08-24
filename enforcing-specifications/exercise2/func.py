"""
A module with an incomplete function.

This function was implemented using the backwards-design technique.
Author:Amelia Litvak
Date:07/07/2025
"""
import introcs


def second_in_list(s):
    """
    Returns: the second item in comma-separated list
    
    The final result should not have any whitespace around the edges.
    
    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'
    
    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """
    assert type(s) == str, 'Precondition violation'
    assert introcs.count_str(s,',') >=2
    start=introcs.find_str(s,',')
    end= introcs.find_str(s,',',start+1)
    #print (end)
    slice =s[start+1:end]
    #print (slice)
    result = introcs.strip(slice)
    #print (result)
    return result