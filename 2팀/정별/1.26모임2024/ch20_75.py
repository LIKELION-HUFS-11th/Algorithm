def maxSlidingWindow(self, nums, k):
    if not nums:
        return nums
    
    r = []
    for i in range(len(nums) - k+1):
        r.append(max(nums(i:i+k)))
    
    return r