""" Given a roman numeral, convert it to an integer. """

class Solution(object):
    def romanToInt(self, s):
        roman = {'M': 1000, 
                 'D': 500, 
                 'C': 100, 
                 'L': 50, 
                 'X': 10, 
                 'V': 5, 
                 'I': 1}
        lst = []
        for el in s:
            if el in roman:
                lst.append(roman[el])
        i = 0
        while i < len(lst) - 1:
            if lst[i] < lst[i+1]:
                lst[i] = lst[i + 1] - lst[i]
                del lst[i + 1] 
            else:
                i += 1
        return sum(lst)
