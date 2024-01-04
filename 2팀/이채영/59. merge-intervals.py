class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # intervals.sort(key = lambda x: x[0]) #intervals[i][0] <= intervals[i+1][0] 보장

        # results = []
        # overlapped = False #직전에 겹치는 상태였는지 기록

        # if len(intervals) == 0 or len(intervals) == 1:
        #         return intervals

        # for i in range(len(intervals)-1):
            
        #     start, end = intervals[i+1][0], intervals[i][1]

        #     if end >= start: #intervals[i]와 intervals[i+1]은 겹치는 구간 존재-> 그 조건의 일부일 뿐임.

        #     if merged_start:
        #         if i == len(intervals)-2:
        #             merged_start, merged_end = intervals[i][0], intervals[i+1][1]
        #             results.append([merged_start, merged_end])

        #         if not overlapped: #겹치는 구간이 이제 시작됨 => overlapped = False
        #             merged_start, merged_end = intervals[i][0], max(intervals[i][1], intervals[i+1][1])
        #             overlapped = True
        #         else: #최소 intervals[i-1]에서부터 겹치는 구간 이어짐
        #             merged_end = max(intervals[i][1], intervals[i+1][1])
        #         #두 상태 모두 겹치는 구간이 intervals[i+1]에서 계속 이어질 수도 있으니, 겹치는 구간의 시작점과 끝점만 조정한다.
            
        #     else: #intervals[i]와 intervals[i+1]은 겹치는 구간 없음
        #         if i == len(intervals)-2: #이렇게 되면 일단 제일 마지막 구간은 겹치지않는 것이 확정됨
        #             not_merged_list = [intervals[i+1][0], intervals[i+1][1]]
        #             results.append(not_merged_list)

        #         if overlapped: #직전까지는 겹치는 구간이었음 -> intervals[i-1]까지 겹치는 구간 종료됨 확정
        #             merged_list = [merged_start, merged_end]
        #             results.append(merged_list)
        #             overlapped = False
        #         else: #intervals[i-1]과 겹치는 구간 없음 -> intervals[i]는 겹치지 않는 것이 확정됨
        #             not_merged_list = [intervals[i][0], intervals[i][1]] #인덱스 i임 주의
        #             results.append(not_merged_list)


        #     # print(merged_start, ",", merged_end)
        #     # results.append(merged_list) #매번 append하면 안되지

        # # for elem in results:
        # #     if elem[0] == -1:
        # #         results.remove(elem)

        # return results

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
        

                
