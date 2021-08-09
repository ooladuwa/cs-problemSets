"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0
Notes:

The input integer will not be negative.
[execution time limit] 4 seconds (py3)

[input] integer n

[output] integer
"""

"""
Understand:
- given an integer...
    - convert to binary
    - reverse binary
- return character representation of reversed binary
"""

def csReverseIntegerBits(n):
    #convert n to binary
    n = bin(n)
    n = n[2:]
    n = n[::-1]
    n = "0b" + n 
    
    return int(n, 2)


