from collections import deque
import sys
input = sys.stdin.realine

def bfs(s):
    q = deque()
    visited = [0 for _ in range(n+1)] # 방문한 노드 표시

    q.append(s) # 큐에 시작노드 넣기
    visited[s] = 1 # 시작노드 방문했다고 표시하기

    while q: # 큐가 비어있지 않은 동안
        x = q.popleft() # 큐에서 하나 꺼내기

        for i in tree[x]: # 해당 노드에 연결된 모든 노드 확인
            if visited[i] == 0: # 방문하지 않은 노드라면
                visited[i] = 1 # 방문표시 하기
                result[i] = result[x] + 1 # 이전 노드로브터의 거리에 1 더한 값을 결과 리스트에 저장
                q.append(i) # 방문하지 않은 노드 큐에 넣기

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수 계산해야 하는 두 사람
m = int(input()) # 부모 자식들 간의 관계의 개수
tree = [[] for _ in range(n+1)] # 그래프
result = [0 for _ in range(n+1)] # 시작 노드부터의 거리 저장

for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

bfs(a)
if result[b] != 0: # 목적지 노드 b에 도달했다면
    print(result[b]) # 정답 출력
else: # 도달하지 못했다면
    print(-1) # -1 출력