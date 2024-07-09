import sys
input = sys.stdin.readline
from collections import deque

'''
[BFS] or [플로이드 워셜]
[BFS]
1. 각 사람마다 BFS 돌려 친구들에게 도달하는 최단 거리 탐색
2. 최단 거리 : 튜플의 두 번째 원소에다 저장
3. 트리가 한 칸씩 깊어질 때마다(=거리가 늘어날 때마다) idx + 1해서 데크에 저장
'''

n, m = map(int, input().split())
relationships = [[] for _ in range(n+1)] # 관계성. relationships[x] : x의 친구들
kb = float('inf') # 최소 케빈 베이컨 초기화
ans = n+1 # 출력할 정답 초기화

for _ in range(m):
    a, b = map(int, input().split())
    relationships[a].append(b)
    relationships[b].append(a)

def bfs(x):
    global kb, ans
    temp_kb = [0] * (n+1) # 현재 x의 각 친구들에 대한 케빈 베이컨을 담을 리스트
    q = deque()
    q.extend([(r, 1) for r in relationships[x]]) # x의 친구들을 데크에 저장. (친구, 거리). 직접 친구이니 거리는 1
    
    while q:
        target, idx = q.popleft()
        if temp_kb[target] == 0 and target != x: # 아직 방문 안했고(temp_kb가 0) + 자기 자신과 같지 않다면
            temp_kb[target] = idx # 현재 x의 친구 target에 대한 케빈 베이컨 기록
            q.extend([(r, idx+1) for r in relationships[target]]) # target의 친구들을 데크에 저장
            
    total = sum(temp_kb) # x의 케빈 베이컨
    if total < kb: # 현재 케빈 베이컨보다 x의 케빈 베이컨이 작다면 업뎃
        kb = total
        ans = x
    # print(x, temp_kb)
        

for i in range(1, n+1):
    bfs(i)

print(ans)



