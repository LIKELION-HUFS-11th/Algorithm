import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(1, k):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)