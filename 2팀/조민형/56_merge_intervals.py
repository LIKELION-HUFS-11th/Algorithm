class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # lambda를 이용해서 첫 각 리스트 첫 번째 수로 정렬
        sortedList = sorted(intervals, key = lambda x : x[0])
        i = 0

        while i < len(sortedList):
            if len(sortedList) == 1:
                break
            if i == len(sortedList)-2:
                if sortedList[i][1] >= sortedList[i+1][0]:
                    newList = [sortedList[i][0],max(sortedList[i+1][1], sortedList[i][1])]
                    sortedList[i] = newList
                    del sortedList[i+1]
                    break
                else:
                    break

            if sortedList[i][1] >= sortedList[i+1][0]:
                newList = [sortedList[i][0],max(sortedList[i+1][1], sortedList[i][1])]
                sortedList[i] = newList
                del sortedList[i+1]
                i -= 1

            i+=1

        return sortedList