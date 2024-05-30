from collections import deque

n, k =map(int, input().split())
def bfs(start, target):
    
    queue = deque([[start, 0]]) #[위치, 시간]. 맨 앞에서부터 차례로 살필 큐
    visited = set([start]) #중복 포함안되게 집합으로 표현.
    # print(queue)
    while queue:
        loc_time = queue.popleft() #queue에서 위치, 시간 뽑기
        loc, time = loc_time[0], loc_time[1]
        if loc == target: #찾았으면 시간 반환
            return time
        
        #걷는 경우 2개, 순간이동하는 경우 1개 총 3개를 모두 탐색해 큐에 추가
        #BFS
        for next_loc in (loc -1 , loc+1, loc*2):
            if next_loc not in visited and 0<= next_loc <= 1000000:
                #범위 안에 있거나, 첫방문이면 왠만해선 추가.
                    visited.add(next_loc) #방문 여부에 위치 추가
                    queue.append((next_loc, time+1))
            # elif next_loc == target:
            #     # time +=1
            #     return time

print(bfs(n, k))
