# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pos = len(nums) // 2
        while nums[pos] != target and left <= right:
            if target > nums[pos]:
              left = pos + 1
            else:
              right = pos - 1
            
            pos = (left + right)//2

        return -1 if left > right else pos


