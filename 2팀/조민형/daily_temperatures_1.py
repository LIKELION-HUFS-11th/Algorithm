class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []
        i = 0
        while i < len(temperatures):
            j = i+1
            a = 0
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    a += 1
                    temp.append(j-i)
                    break
                j += 1
            if a == 0:
                temp.append(0)
            i += 1

        return temp
