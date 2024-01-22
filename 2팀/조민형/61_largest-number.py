class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_copy = nums[:]
        i = 0
        newNum_temp = []
        
        while i < len(nums):
            j = 0
            maxNum = 0    
            maxj=0
            while j <= len(newNum_temp):
                newNum_temp.insert(j,str(nums[i]))
                newmax = "".join(newNum_temp)
                if int(maxNum) < int(newmax):
                    maxNum = newmax
                    maxj = j
                del newNum_temp[j]
                j += 1
            newNum_temp.insert(maxj, str(nums[i]))
            i += 1

        if int("".join(newNum_temp)) == 0:
            return "0"
        
        return "".join(newNum_temp)
                