Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.

"""
UNDERSTAND:
- identify vowels and remove them from a given string. 
- return string minus the vowels.

PLAN:
create an empty string
iterate over each character in string for vowels
append non-vowel characters to new empty string
return new string to caller

"""

def csRemoveTheVowels(input_str):

    result = ""

    for c in input_str:
        if c.lower() not in "aeiou":
            result += c

    return result
