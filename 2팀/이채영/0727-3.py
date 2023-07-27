class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        plus = []
        minus = []
        is_zero = False

        for elem in nums:
            if elem < 0:
                minus.append(elem)
            elif elem > 0:
                plus.append(elem)
            else:
                is_zero = True


        result = []
        for elem in plus:
            for i in range(len(minus)):
                for j in range(i+1, len(minus)):
                    if minus[j] == minus[i]:
                        continue
                    if minus[i] + minus[j] + elem == 0:
                        result.append([minus[i], minus[j], elem])
        
        for elem in minus:
            for i in range(len(plus)):
                for j in range(j+1, len(plus)):
                    if plus[i] == plus[j]:
                        continue
                    if elem + plus[i] + plus[j] == 0:
                        result.append([elem, plus[i], plus[j]])
        
        if is_zero:
            for i in range(len(plus)):
                if 
                for j in range(len(minus)):
                    if plus[i] + minus[j] == 0:
                        result.append([minus[j], 0, plus[i]])

        return result
