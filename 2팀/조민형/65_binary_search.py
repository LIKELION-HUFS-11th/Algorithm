

# 재귀적으로 푼 방법
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def binary(left,right) :
#             if left <= right:
#                 mid = (left + right) // 2

#                 while left<=right:
#                     if nums[mid] == target:
#                         return mid
#                     elif nums[mid] < target:
#                         return binary(mid+1, right)
#                     elif nums[mid] > target:
#                         return binary(left, mid-1)
#             else: return -1

#         return binary(0,len(nums)-1)
                