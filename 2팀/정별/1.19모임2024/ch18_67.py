class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1 = set(num1)
        # num2 = set(num2)
    
        nInter: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    nInter.add(n1)
        
        return nInter



#민형이 풀이
# 44ms, 89.86% beat
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1= set(nums1)
        nums2= set(nums2)
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result

# 86ms, 9.89% beat
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#         for i in nums1:
#             for j in nums2:
#                 if i==j and i not in result:
#                     result.append(i)
        
#         return result
    
# 62ms, 23.91% beat
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#         for i in nums1:
#             if i in nums2 and i not in result:
#                 result.append(i)
        
#         return result
