"""
Module with simple for-loop functions.

Author: Amelia Litvak
Date: 08/12/2025
"""


def lesser(tup,value):
    """
    Returns the number of elements in tup strictly less than value
    
    Examples: 
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0
    
    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints
    
    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    counter=0
    for string in tup:
        if string<value:
            counter+=1
    return counter



def avg(tup):
    """
    Returns average of all of the elements in the tuple.
    
    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.
    
    Examples: 
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5
    
    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    counter=0
    result=0.0
    for value in tup:
        counter=counter+value
    if len(tup)>0:
        result=counter/len(tup)    
    return result
