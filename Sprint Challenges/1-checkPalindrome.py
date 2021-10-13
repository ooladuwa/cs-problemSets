"""
check in string is a palindrome
return True if Yes
return False if No

Plan:
    
"""

def csCheckPalindrome(input_str):
# initiate length of string 
    l = int(len(input_str))
# iterate through array forwards
    for i in range(l):
        # compare left to right starting with index[0] and index[-1]
        if input_str[i] != input_str[i-1]:
            # return false first time condition not met
            return False
        # return true once loop completes
        return True

