def arrayPairSum(self, nums: list[int]) -> int:
    nums.sort()

    i = 0
    total = 0
    while i <= len(nums):
        a = [nums[i], nums[i+1]]
        
        total += min(a)
        i += 2

    return total
