n, m = map(int, input().split())

min_num, max_num = 0, 0
for i in range(n):
    nums = list(map(int, input().split()))
    min_num = min(nums)
    max_num = max(max_num, min_num)

print(max_num)

