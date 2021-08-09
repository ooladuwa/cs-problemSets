You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.

"""
Understand:
- in a given string, identify all the parentheses
- return true if count of "(" matches count of ")"
- return false is the counts do not match
"""

def validParenthesesSequence(s):
    openP = 0
    closeP = 0
    for char in s:
        if s[0] == "(" and char == "(":
            openP += 1
        elif s[len(s)-1] == ")" and char == ")":
            closeP += 1

    if openP == closeP:
        return True
    return False