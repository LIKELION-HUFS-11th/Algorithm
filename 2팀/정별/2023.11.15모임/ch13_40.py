import collections, heapq

class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        
        #그래프를 인접 리스트로 표현하는 딕셔너리 생성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        #우선순위 큐 활용을 위한 큐의 변수 정의
        Q = [(0, k)] #[(시작점에서 정점까지의 소요시간, 정점)]
        dist = collections.defaultdict(int) #거리.여기서 정답 return 할 예정

        while Q:
            time, node = heapq.heappop(Q)#최소힙에서 최솟값 추출(자동으로 우선순위 큐 구현)
            if node not in dist: #노드 포함여부 확인. 최소힙 구조니까 최솟값 먼저 할당하고, 그 이후에 중복되는건 포함 안시킴
                dist[node] = time
                for v, w in graph[node]: #graph의 value 값 돌기. BFS 표현.(node값은 고정되어 있으니, 할당된 node 값 출발)
                    alt = time + w
                    heapq.heappush(Q, (alt, v)) #힙구조로 Q에 소요시간과 노드 이름이 들어감
        
        if len(dist) == n: #총 노드 개수와 일치하는지 검증. 모자란다면 시작노드에서 모든 노드까지 도달할 수 없다는 뜻임.
            return max(dist.values()) #가장 오래 걸리는 노드까지의 최단 시간 출력
        return -1

if __name__ == '__main__':
    s = Solution()
    ans1 = s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
    ans2 = s.networkDelayTime([[1,2,1]], 2, 1)
    ans3 = s.networkDelayTime([[1,2,1]], 2, 2)
    
    print(ans1, ans2, ans3)