Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.


"""
UNDERSTAND:
- take in an input string
- test input string to ensure it contains only alpha characters

- return input string with:
    - input string in reverse order
    - each character in input string has opposite casing

PLAN:
will utilize python reversed function to reverse the string and swapcase method to reverse casing: 

create empty string
reverse string
reverse casing

return created string
"""


def csOppositeReverse(txt):
    result = ""
    for c in reversed(txt):
        result += c
    
    return result.swapcase()
    