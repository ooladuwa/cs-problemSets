"""
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
Notes:

The score of the students is between 1 and 100.
"""

"""
- take in an array of arrays
    inner arrays are [student_id, student_score]
- for each student_id, get average score
-return [student_id, average_score]
"""
def csAverageOfTopFive(scores):
    freq = {}
    result = []
    
    for i in range(len(scores)):
        student, score = scores[i]
        
    # check for key in freq and if not there create new list
    # append score to list at student key
        if student not in freq:
            freq[student] = []
        freq[student].append(score)
    
    for student, score in freq.items():
        score = sorted(score, reverse = True)[:5]
        average = sum(score) // len(score)
        
        result.append([student, average])
    
    return result
        
        
        
    
    
    
    # d = {}
    # s = sorted(scores)    
    # count = 0
    # for result in s:
    #     s_id = result[0]
    #     score = result[1]
    #     if s_id not in d:
    #         d[s_id] = []
    #         d[s_id].append(score)
    #     else:
    #         d[s_id].append(score)
    # print(d)
    
    # total = 0
    # for key, value in d.items():
    #     split = len(value)
    #     total = sum(d[s_id])
    # print(total)
    # print(split)
        
        # print(type(value))
        # total = sum(value)
        # length = len(key.value)
        # print(length)
        # print(total)
    #     num = len(value)
    #     print(num)
   
        # if s_id in d:
        #     if not isinstance(d[s_id], list):
        #         d[s_id] = [d[s_id]]
        #     d[s_id].append(score)
        # else:
        #     d[s_id] = (score)