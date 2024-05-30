import sys
input = sys.stdin.readline
import heapq

'''
[우선순위큐(힙큐) + bfs]
1. s초 뒤의 (x, y) 지점에 있는 바이러스 종류 구하는 것이 목표
2. 바이러스는 상, 하, 좌, 우로 퍼지며 숫자 낮은 바이러스가 우선
'''

n, k = map(int, input().split())
viruses = []
for _ in range(n):
    viruses.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

da, db = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs():
    temp = []
    for i in range(n):
        for j in range(n):
            if viruses[i][j] > 0:
                heapq.heappush(temp, [viruses[i][j], i, j]) # 시작시점에서의 바이러스들 종류, 위치 저장(바이러스 숫자 낮은 것부터)
    for _ in range(s):
        q = temp # q 업데이트
        temp = [] # temp 초기화
        while q: # 현재 시점에 돌 수 있는 좌표들 다 돌기
            value, a, b = heapq.heappop(q) # 바이러스 숫자 낮은 것부터 pop
            for k in range(4):
                na, nb = a+da[k], b+db[k] # 해당 바이러스의 상, 하, 좌, 우
                if 0<=na<n and 0<=nb<n and viruses[na][nb] == 0: # 좌표 안 & 아직 전염되지 않은 칸이면
                    viruses[na][nb] = value # 전염시키기
                    heapq.heappush(temp, [value, na, nb]) # 다음 시점에 돌 좌표들을 temp에 저장
    return viruses[x-1][y-1]
    
print(bfs())