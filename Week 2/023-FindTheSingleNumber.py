"""
You are given a non-empty array of integers.

One element appears exactly once, with every other element appearing at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.
"""

"""
Understand:
find the single, non-repeating number in an array
"""
def csFindTheSingleNumber(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]
    
    
    
    
    
    
    
    
    # # enumerate array for i, num and iterate through
    # for i, char in enumerate(nums):
    #     # if not in slice before character AND
    #     # if not in slice after character
    #     if char not in nums[:i] #and nums[char:]:
    #         print("b4 char:", nums[:i])
    #         print(char, i)
    #         print("after char:", nums[i:])
    #         continue
    #         # return char
    # #return char