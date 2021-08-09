Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".


"""
Understand:
-given a string, replace each letter in the string with the next letter alphabettically

Plan:
- create alphabet string and enumerate it
- create new blank string
- iterate through inputString
  - for each inputLetter, get index of same letter from alphabet and append alphabet index+1 to new string
- return new string 
"""

def alphabeticShift(inputString):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    new=[]
    for i in range(len(inputString)):
        if inputString[i] == "z":
            new.append(0)
        else:
            new.append(alpha.index(inputString[i])+1)
        
    for i in range(0, len(new)):
        s += alpha[new[i]]
        
    return s
    
