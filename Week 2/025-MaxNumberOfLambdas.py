"""Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1
Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2
Example 3:

Input: text = "sctlamb"
Output: 0
Notes:

text consists of lowercase English characters only
"""

def csMaxNumberOfLambdas(text):
    # sub_string = "lambda"
    word = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0, 'a': 0}
    counts = []
    for letter in text:
        if letter in word:
            word[letter] += 1
    for key, value in word.items():
        counts.append(value)
    return min(counts)
    
    
    
    
    # d = {"l": 0, "a": 0, "m": 0, "b": 0, "d": 0, "a":0}
    # result = []
    
    # for c in text:
    #     if c in d:
    #         d[c] = text.count(c)
    # print(d)
        
    
    # for key, value in range(len(d)):
    #     print(key, value)
    #     result.append(value)
    #     print(result)
            
    # return min(result)
    
    
# def csAverageOfTopFive(scores):
#     freq = {}
#     result = []
    
#     for i in range(len(scores)):
#         student, score = scores[i]
        
#     # check for key in freq and if not there create new list
#     # append score to list at student key
#         if student not in freq:
#             freq[student] = []
#         freq[student].append(score)
    
#     for student, score in freq.items():
#         score = sorted(score, reverse = True)[:5]
#         average = sum(score) // len(score)
        
#         result.append([student, average])
    
#     return result