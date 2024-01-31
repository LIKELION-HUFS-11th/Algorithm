class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #여러번 거래 가능 -> 횟수에 상관 없이 항상 이익을 내면 됨 -> 내리기 전에 팔고, 오르기 전에 사기 (그리디)

        min_val = prices[0]
        max_rev = 0
        total = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]: #가격 오름 : 수익 = 현재가격 - 이전 가격
                max_rev = max(max_rev, prices[i]-min_val)
            else: #가격 오르지 않음 -> 최고수익 저장 + 최소구매가격 조정
                min_val = prices[i]
                total += max_rev #팔기
                max_rev = 0 #고점이 아님 -> 최고수익 불가능

        return total + max_rev

        #####sol2. 
        # result = 0
        # for i in range(len(prices)-1):
        #     if prices[i+1] > prices[i]: # 가격 상승
        #         result += prices[i+1] - prices[i]
        
        # return result

            
