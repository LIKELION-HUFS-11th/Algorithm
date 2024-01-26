from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # #Sol 1
        # if not nums:
        #     return nums

       
        # result = []
        # for i in range(len(nums)-k+1):
        #     j = i + (k - 1)
        #     result.append(max(nums[i:j+1]))

        # return result

        #Sol 2
        results = []
        window = deque()   

        for _ in range(k):
            window.put(nums.pop()) #[1, 3, -1]
        
        for _ in range(len(nums)-k):
            result.append(max(window))
            window.popleft()
            window.append(nums.pop())

        return result
