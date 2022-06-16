
"""Given an integer x, return true if x is palindrome integer."""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = {}
        if  x < 10 and x > -1:
            return True
        i = 0
        while x > 0:
            nums[i] = x%10
            x //= 10
            i += 1
        a = ceil(len(nums)//2)
        for i in range(a):
            if nums[i] == nums[len(nums) - i - 1]:
                if i == a - 1:
                    return True
                continue
            else: 
                return False



