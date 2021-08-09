Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9

#UNDERSTAND:
# given integer, return square of EACH DIGIT

#PLAN
# create empty string
#turn integer into string
# iterate through string creating an integer of each digit
# square each digit
# append squared digit to created string

def csSquareAllDigits(n):
    result = ""
    
    for c in str(n):
        result += str(int(c) ** 2)
    
    return int(result)