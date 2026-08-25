"""  
A function to extract names from e-mail addresses.

Author: Amelia Litvak
Date: 08/08/2025
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.
    
    We assume (see the precondition below) that the e-mail address is in one of
    two forms:
        
        last.first@megacorp.com
        first.last@mompop.net
    
    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed 
    to be exactly as shown.
    
    The function preserves the capitalization of the e-mail address.
    
    Examples: 
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'
    
    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-else statement in this function.
    point=introcs.find_str(s,'@')
    period=introcs.find_str(s,'.')
    first_name=s[0:period]
    last_name=s[period+1:point]
    domain_name=s[point+1:]
    if  domain_name=='mompop.net':
        return first_name
    else:
        return last_name
