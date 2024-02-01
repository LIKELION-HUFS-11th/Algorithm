class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import heapq

        heap = []
        #내림차순 정렬 heappush
        for i in people:
            heapq.heappush(heap,(-i[0],i[1]))
        
        result = []
        while heap:
            #하나씩 큰 순서부터 작은 순서까지 앞에서 빼내기
            person = heapq.heappop(heap)
            #결과 리스트에 위치대로 넣어주기
            result.insert(person[1], [-person[0],person[1]])
        return result
        