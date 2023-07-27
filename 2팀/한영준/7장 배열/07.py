nums = [3, 3]
target = 6
hap = 0
index = []
for i in range(len(nums)-1):
    for k in range(1, len(nums)):
        hap = nums[i] + nums[k]
        if hap == target:
            index.append(i)
            index.append(k)
            break

print(index)
