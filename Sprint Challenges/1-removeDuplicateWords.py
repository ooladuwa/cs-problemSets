"""
Understand:
return one occurance of each word in the string as a string separated by ONLY a space(no comma)
"""
def csRemoveDuplicateWords(input_str):
    #split string
    first = input_str.split()
    
    # join and sort newly created set
    second = " ".join(sorted(set(first), key=first.index))   
    
    return(second)


