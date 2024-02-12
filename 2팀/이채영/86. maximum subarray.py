class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = [0] * len(nums)
        S[0] = nums[0]
        for i in range(1, len(nums)):
            S[i] = max(S[i-1] + nums[i], nums[i])
        
        return max(S)