Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"

"""
Understand: 
take two strings of lowercase char
return new sorted string with all char from string 1 and 2 with no repeats

Plan:
- create a new sorted list containing str_1 & str_2
- iterate through newString by i
    if char in newString == newString[i]
    remove char
    continue 
- return newString
"""
def csLongestPossible(str_1, str_2):
    new = set(str_1 + str_2)
    return "".join(sorted(new))
    