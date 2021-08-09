Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.

"""
UNDERSTAND:
given a string, return a boolean based on whether it contains all numbers, letters, or a combination of both. Must think about non letter or number values which will return false.

PLAN: 
create variable s = "string"
#convert string to list
    iterate through s 
        if all elements are type 'letter', return True
        if all elements are type 'number', return True
        if elements contain different types, return False
        if element contains type other than 'letter' or 'number', return False
        if element is blank, return False
        if s contains spaces, return False
        
        
take in an input string, test if the input string is ...
    return either only letters and no numbers, or only numbers and no letters
    
    input: input_str: => str
    output: => boolean
"""

def csAlphanumericRestriction(input_str):
    
    return input_str.isalpha() or input_str.isnumeric()