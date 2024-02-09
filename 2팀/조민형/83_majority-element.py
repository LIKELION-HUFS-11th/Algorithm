class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counterNums = Counter(nums)
        for i in counterNums:
            if counterNums[i] > (len(nums)//2):
                return i