nums = [1, 4, 3, 2]
nums.sort()
nums.reverse()
hap = 0

for i in range(0, len(nums)-1, 2):
    hap = hap + min(nums[i], nums[i+1])

print(hap)
