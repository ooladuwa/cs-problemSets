def findValueSortedShiftedArray(nums, target):
    # if target in nums:
    #     return nums.index(target)
    # return -1
    
    sNums = sorted(nums)
    end = len(nums)-1
    start = 0
    mid = (end - start) //2
    
    while not end < start:
        guess = (end - start) // 2
        if sNums[guess] == target:
            return nums.index(sNums[guess])
        elif sNums[guess] < target:
           begin = guess + 1
        else:
            end = guess -1      
    return -1
    
    
"""
You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""