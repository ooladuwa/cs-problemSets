"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

All elements in nums are unique.
The length of nums will be <= 100
The value of each element in nums will be in the range [1, 10000]
"""

def csBinarySearch(nums, target):
    # Binary search
    
    #keep track of begin and end
    #while the begin and end do not overlap:
        # create a guess index in the middle of the view of the data
        # check if the data at the guess index is equal to the target
            #return(guess_index, guess)
        #otherwise is the data at the guess index less than the target
            #set the begin to the guess index +1
        #otherwise
            #set the end to the guess index -1
    #if we get here we can not find the target
    #return -1
    
    begin = 0
    end = len(nums) -1
    while not end < begin:
        guess_index = (end + begin) // 2
        if nums[guess_index] == target:
            return (guess_index)
        elif nums[guess_index] < target:
            begin = guess_index + 1
        else:
            end = guess_index -1
            
    return -1
    
    
    # linear search:
    
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # return -1
    
        
    
