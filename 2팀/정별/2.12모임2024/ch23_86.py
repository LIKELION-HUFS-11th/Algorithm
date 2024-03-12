class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        cur_sum = 0

        for n in nums:
            cur_sum = max(n, cur_sum + n)
            best_sum = max(best_sum, cur_sum)
        
        return best_sum