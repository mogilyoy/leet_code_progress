# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution(object):
    def longestPalindrome(self, s):
        qua = {}
        count = 0
        for i in s: 
            if i in qua:
                qua[i] += 1
            else:
                qua[i] = 1
        print(qua)
        yes = list(qua.values())
        for i in range(len(yes)):
            count += yes[i]//2
            yes[i] = yes[i]%2
        count = 2*count

        if 1 in yes:
            count += 1
        return count
        


if __name__ == '__main__':
    sol = Solution()
    a = sol.longestPalindrome('ccdd')
    print(a)