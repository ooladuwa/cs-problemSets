Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.

def csShortestWord(input_str):
    words = []
    for word in input_str.split():
       words.append(len(word))
    return min(words)