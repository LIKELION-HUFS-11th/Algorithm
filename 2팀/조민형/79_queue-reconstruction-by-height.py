class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import heapq

        heap = []
        # 키 내림차순으로 정렬해서 push하기
        for i in people:
            heapq.heappush(heap,(-i[0],i[1]))
        
        result = []
        # 내림차순으로 된 heap에서 하나씩 빼가면서 해당 위치에 끼워넣기
        while heap:
            person = heapq.heappop(heap)
            result.append(person)
            print(result)
        