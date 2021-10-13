    #Tom's solution

def dft(friendships, visited, i):
    for j in range(len(friendships)):
        if friendships[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dft(friendships, visited, j)

def csFriendCircles(friendships):
    visited = [0] * len(friendships)
    print(visited)
    count = 0
   
    for i in range(len(friendships)):
        if visited[i] == 0:
            dft(friendships, visited, i)
            count += 1
           
    return count
    
    #Tony's solution
    
# def csFriendCircles(friendships):
#     count = 0
# #create a seen set variable
#     seen = set()
# #create a dfs function (person)
#     def dfs(person):
# #loop through friendships
#         for i in range(len(friendships)):
#             if friendships[person][i] and i not in seen: 
# #if friendships[person][i] and i not in seen
# #add to our seen set.
#                 seen.add(i)
#                 dfs(i)
#                 print(friendships[person][i])

#     for i in range(len(friendships)):
#         if i not in seen:
#             count +=1
#             seen.add(i)
#             print(seen)
#             dfs(i)
#     return(count)



"""
There are N students in a baking class together. Some of them are friends, while some are not friends. The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students who are either direct or indirect friends of some level. That is, the friend circle consists of a person, their friends, their friends-of-friends, their friends-of-friends-of-friends, and so on.

Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

You need to write a function that can output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation: The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation: The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
[execution time limit] 4 seconds (py3)

[input] array.array.integer friendships

[output] integer
"""