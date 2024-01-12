class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2 #index
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)


        return binary_search(0, len(nums)-1)