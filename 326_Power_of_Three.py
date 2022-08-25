# 326. Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true

from math import log
from random import randint

class Solution(object):
    def isPowerOfThree(self, n):
        log3 = 1.0986122886681098
        if n <= 0:
            return False
        logg = log(n)/log3
        around = round(logg, 2)
        if abs(logg - around) < 4e-15:
            return True
        else:
            return False


if __name__ == '__main__':
    for i in range(1, 21):
        b = randint(0, 3)
        m = 3 ** i - b
        sol = Solution()
        a = sol.isPowerOfThree(m)
        if a:
            print(a, m, b)
        else:
            print('х', b)






