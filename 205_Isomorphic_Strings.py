# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.
# Input: s = "paper", t = "title"
# Output: true
# Input: s = "foo", t = "bar"
# Output: false


class Solution(object):
    def isIsomorphic(self, s, t):
        d = {}
        flag = True
        lenght = len(s)
        try:
            for i in range(lenght):
                if s[i] not in d and t[i] not in list(d.values()):
                    d[s[i]] = t[i]
        except KeyError:
            flag = False
        return flag


if __name__ == '__main__':
    sol = Solution()
    a = sol.isIsomorphic('badc', 'baba')
    print(a)

