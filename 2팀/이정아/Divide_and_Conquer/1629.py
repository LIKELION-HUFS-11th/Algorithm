a, b, c = map(int, input().split())
nums = []
num = 1
rep = False
for _ in range(b):
    if num * a % c in nums:
        if num * a % c == nums[-1]:
            rep = True
        break
    nums.append(num * a % c)
    num *= a
if rep:
    print(nums[-1])
else:
    print(nums[b%len(nums)-1])