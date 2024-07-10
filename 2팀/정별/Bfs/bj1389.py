#참고링크: https://donghak-dev.tistory.com/10
import sys
#간선 존재하는지, 길이 얼마인지 계산.

INF = int(1e9)

N, M = map(int, input().split())

relation = [[INF] * N for _ in range(N)]

for i in range(N):
    relation[i][i] = 0

for _ in range(M):
    start, end = map(int, input().split())
    relation[start-1][end-1] = 1
    relation[end-1][start-1] = 1
    
for k in range(N):
    for a in range(N):
        for b in range(N):
            relation[a][b] = min(relation[a][b], relation[a][k]+relation[k][b])

answer = INF #현재까지 발생한 최소 거리 합
index = INF #최소 거리 합을 가진 노드의 인덱스 저장
for i in range(len(relation)):
    if sum(relation[i]) < answer: #노드'i'에서 다른 모든 노드로의 거리 합
            #그 합이 지금까지 발견된 최소 거리 합보다 작음.
        answer = sum(relation[i])
        index = i
print(index+1)