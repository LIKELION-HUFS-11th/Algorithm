class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        merged = []
        intervals.sort(key = lambda x: x[0]) #intervals[i][0] <= intervals[i+1][0] 보장

        #뒷구간은 아예 신경쓰지 않기.
        for i in intervals:
            if merged and i[0] <= merged[-1][1]:
                if merged and i[0] <= merged[-1][1]: # intervals[i]에서 겹치는구간 이어짐
                    merged[-1][1] = max(merged[-1][1], i[1])  #구간의 끝점을 특정 포인트로 보면 힘들어짐 -> 가능한 끝점 후보들 중 최대값으로 쓰기
            else:
                merged.append(i) #intervals[i-1]까지와 겹치지 않는다면 일단 새 구간 시작
        return merged

        # O(nlogn) + O(n) = O(nlogn) 소요
        

                
