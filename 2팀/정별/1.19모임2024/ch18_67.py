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
