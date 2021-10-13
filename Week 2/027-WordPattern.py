"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
a contains only lower-case English letters and spaces ' '.
a does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
"""

"""
Understand: 
- take in a pattern and a string
- determine if string follows same structure as pattern
"""

def csWordPattern(pattern, a):
    comp = {}
    
    a = a.split()
    # print(a)

    if len(pattern) != len(a):
        return False
    
    if len(a) < 2 or len(pattern) < 2:
        return True
        
    for i in range(len(a)):
      
        if pattern[i] not in comp:
            if a[i] in comp.values():
                return False
            comp[pattern[i]] = a[i]
            # print("first loop")
            # print(comp)
            
        else:
            print(comp[pattern[i]])
            print(a[i])
            if comp[pattern[i]] != a[i]: 
                return False
            # if comp[pattern[i]] == a[i]:
            #     continue
            # if :
            #     return False  
            
    return True
