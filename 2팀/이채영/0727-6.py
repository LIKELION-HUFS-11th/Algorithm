import sys 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_buy = sys.maxsize
        max_profit = 0 # sell 아니고 profit

        for i in range(len(prices)):
            if i < len(prices)-1:
                min_buy = min(min_buy, prices[i])
            if i > 0:
                max_profit = max(max_profit, prices[i]-min_buy)

        return max_profit