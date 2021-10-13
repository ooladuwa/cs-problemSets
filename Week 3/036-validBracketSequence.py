def validBracketSequence(sequence):
    # edge: len of sequence = 0 => True
    if len(sequence) == 0:
        return True
    # edge: if len(sequence) is odd => False
    if len(sequence) % 2 != 0:
        return False
    
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"]
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    stack = []
    
    for ch in sequence:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if not stack or pairs[stack.pop()] != ch:
                return False            
    return len(stack) == 0
   

   """
   Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
"""