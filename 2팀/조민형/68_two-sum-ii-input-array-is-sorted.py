#105msm 86% beat
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right =len(numbers)-1
        result =[]
        while left<right:
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            elif numbers[left] + numbers[right] < target:
                left+=1
                continue
            elif numbers[left] + numbers[right] == target:
                result.append(left+1)
                result.append(right+1)
                break

        return result



            


# 짱느림
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         result = []

#         for i in range(len(numbers)):
#             if target-numbers[i] in numbers and i+1 not in result and numbers.index(target-numbers[i])!=i:
#                 result.append(i+1)
#                 result.append(numbers.index(target-numbers[i])+1)
        
#         result.sort()
#         return result
    
