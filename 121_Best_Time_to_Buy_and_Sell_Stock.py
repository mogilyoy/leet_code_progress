# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
from random import randint


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_income = 0
        cur_min = float('inf')
        cur_max = 0
        for i in prices:
            if i < cur_min:
                cur_min = i
                cur_max = 0
            if i > cur_max:
                cur_max = i
                
            if cur_max - cur_min > max_income:
                max_income = cur_max - cur_min
        return max_income
        


        

if __name__ == '__main__':
    sol = Solution()
    for i in range(10):
        lst = [randint(0, 5) for _ in range(10)]
        print(lst)
        a = sol.maxProfit(lst)
        print(a)