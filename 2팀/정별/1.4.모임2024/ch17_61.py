# class Solution:
#     def largestNumber(self, nums) -> str:

def compare(x,y):
    return str(x) + str(y) < str(y) + str(x)

nums = [3, 30, 34, 5, 9]

strs =[]
for n in nums:
    n = str(n)
    strs.append(n)

sort_strs = sorted(strs, reverse = True)
print(sort_strs)

#람다에다가 함수 적용 어떻게??

