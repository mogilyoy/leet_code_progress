# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

import cProfile

# class Solution(object):
def twoSum(nums, target):
    lenght = len(nums)
    for i in range(len(nums)):
        for j in range(i+1, lenght):
            if nums[i] + nums[j] == target:
                return [i, j]

        
if __name__ == '__main__':
    cProfile.run('twoSum([i for i in range(1000)], 1999)')
    cProfile.run('twoSum([i for i in range(10000)], 19999)')
    cProfile.run('twoSum([i for i in range(100000)], 199999)')


                


