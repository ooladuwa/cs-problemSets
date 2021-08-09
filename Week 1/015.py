Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.

def csFirstUniqueChar(input_str):
    new = {}
    for c in input_str:
        new[c] = input_str.count(c)
        print(new)
        
    for i, c in enumerate(input_str):
        if new[c] == 1:
            return i
    return -1