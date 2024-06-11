import sys
input = sys.stdin.readline

n = int(input())
nStones = list(list(map(int, input().split())) for _ in range(n-1))
nStones = [0]+ nStones #출발점 추가
k = int(input())
# print(nStones)

nAns =[] #정답 후보 담을 리스트

def dfs(nPos_now, nEnergy, vSuper_jmp):
    if nPos_now == n: #도착했다면. #n-1돌 까지 딱 왔을 때는 단순히 1칸 더 움직이고 답 도출임
        nAns.append(nEnergy)
        return
    if nPos_now > n: return #범위 벗어나면
    
    # if not vSuper_jmp and nPos_now+3 < n:
        # vSuper_jmp = True
    if not vSuper_jmp:
        dfs(nPos_now+3, nEnergy+ k, True)
    
    #슈퍼점프 했는지 안했는지 상관없이 일단 1단 2단 점프 다 시도
    # if nPos_now +1 < n: #1단 점프 가능한지
    dfs(nPos_now+1, nEnergy+ nStones[nPos_now][0], vSuper_jmp)
    
    # if nPos_now +2 <n: #2단점프 가능한지
    dfs(nPos_now+2, nEnergy+nStones[nPos_now][1], vSuper_jmp)

dfs(1, 0, False)
# print(nAns)
# if n ==1:
#     print(nStones[1][0])
# else:
print(min(nAns))    
        



# #bfs로 시도하다가 안됨
# from collections import deque

# n = int(input())
# nStones = {}

# for i in range(n-1):
#     x, y = map(int, sys.stdin.readline().split())
#     nStones[i] = [x, y]
# k = int(input())

# # print(nStones)
# nEnergy = 0

# def bfs(nNow, nEnergy):
#     queue = deque([(nNow, nEnergy, False)])
    
#     while queue:
#         cur_pos, cur_energy, used_super_jmp = queue.popleft()
