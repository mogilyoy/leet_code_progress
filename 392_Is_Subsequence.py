# 392. Is Subsequence 
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution(object):
    def isSubsequence(self, s, t):
        flag = [False]*len(s)
        for cur in range(len(s)-1, -1 ,-1):
            for i in range(len(t)-1 , -1, -1):
                if t[i] == s[cur]:
                    t = t[:i]
                    flag[cur] = True
                    break
        for el in flag:
            if not el:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    a = sol.isSubsequence("ace", "baacbe")
    print(a)
