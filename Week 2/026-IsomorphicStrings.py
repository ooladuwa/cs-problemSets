"""
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true
Example 2:

Input:
a = "foo"
b = "bar"

Output:
false
Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true
Example 4:

Input:
a = "abc"
b = ""

Output:
false
"""

"""
Understand:
- take in two strings
- if isomorphic, return true/ else return false
    - isomorphic means that:
        - all instances of a character in string a can be                   replaced in string b with the SAME replacement                  character at the SAME location
"""

def csIsomorphicStrings(a, b):
    comp = {}
    
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] in comp:
                if comp[a[i]] == b[i]:
                    pass
                else: 
                    return False
            else: 
                comp[a[i]] = b[i]
    return True
        
#     # match = []
#     match = []
# # enumerate each string 
#     a = list(a)
#     print(a)

#     # for i, c in enumerate(a):
#     #     if 
#     #     print(i, c)
#     #     if a[i] == c:
#             # print("wheee")
        
#     for i in range(len(a)):
#         print(i, a[i])
        
        
#     # for i, c in enumerate(b):

#     # if a[i] value == value anywhere else, append i and i as list to match
    
#     # do same for b
    
#     # if match object is empty - return True
    
#     # if new[i][0] == new[i+1]
#         # return True
#     # return False
# # find index and value for each character in string b

    