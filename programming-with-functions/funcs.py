"""
The functions for the course project.
Author:Amelia Litvak
Date:07/07/2025
"""
import introcs
def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert type(s)== str
    first_open_paren=introcs.find_str(s,'(')

    first_closed_paren=introcs.find_str(s,')',first_open_paren)

    return first_open_paren != -1 and first_closed_paren != -1

def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str
    print (s)
    first_open_paren=introcs.find_str(s,'(')
    print(first_open_paren)
    first_closed_paren=introcs.find_str(s,')',first_open_paren)
    assert first_open_paren != -1 and first_closed_paren != -1
    print(first_closed_paren)
    in_parens=s[first_open_paren+1:first_closed_paren]
    print(in_parens)
    return in_parens