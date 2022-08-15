# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        
        left = 0
        right = n
        if not isBadVersion(right):
                return -1
        while True:                
                if right - left == 1 and isBadVersion(right) and not isBadVersion(left):
                        return right
                
                mid = (left + right) // 2
                if isBadVersion(mid):
                        right = mid
                else:
                        left = mid


# [2,1,3]
# [5,1,4,null,null,3,6]
# [5,4,6,null,null,3,7]
# [2,2,2]

