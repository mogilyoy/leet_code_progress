# 869. Reordered Power of 2
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.

# Example 1:
# Input: n = 1
# Output: true

# Example 2:
# Input: n = 10
# Output: false


from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, n):
        powers = [Counter('1')]
        pow = 1
        while pow < 10**9:
            pow *= 2
            powers.append(Counter(str(pow)))
        
        for i in powers:
            if i == Counter(str(n)):
                return True
        return False


# с побитовым сдвигом
class Solution:
    def reorderedPowerOf2(self, n):
        digits = Counter(str(n))
        
        for i in range(30): 
            if digits == Counter(str(1 << i)):
                return True
        return False



