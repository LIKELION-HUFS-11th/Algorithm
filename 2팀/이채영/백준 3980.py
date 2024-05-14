import sys
input = sys.stdin.readline

def find_max_total(depth):
    global result

    if depth == 11: #리프노드까지 가면 해당 케이스 탐색 완료.
        result = max(result, sum(pick_players))
        return
    
    for i in range(11): #i=선수 depth=경기회차
        if visited[i] != 0:
            continue
        
        if players[i][depth] != 0:
            visited[i] = 1
            pick_players.append(players[i][depth])
            find_max_total(depth+1)

            pick_players.pop(-1) #백트래킹 - 마지막원소 pop하여 다시 직전 상태로 돌아감 
            visited[i] = 0

n = int(input().strip())
for _ in range(n):
    players = []
    for _ in range(11):
        players.append(list(map(int, input().split())))
    
    result = 0
    pick_players = []
    visited = [0 for _ in range(11)] #선수 0~10 저장

    find_max_total(0)

    print(result)




###
# global max_total, max_ability

# """
# 백트래킹 + 상태공간트리

# 1. 능력치 합의 기대 최대 합이 더 낮으면 후퇴
# 2. 이미 포지션에 세운 선수면 후퇴 
# """

# def find_max_total(depth, total): #depth = 경기회차 (0~10)
#     global max_total, max_ability

#     if depth == 11:
#         return max_total
    
#     if (total + (max_ability * (11 - depth - 1)) < max_total):
#         return
    
#     if total > max_total:
#         max_total = total

#     for i in range(11): # i = 선수 depth = 경기회차
#         if visited[i] != 0:
#             continue

#         if players[i][depth] != 0:
#             visited[i] = 1
#             find_max_total(depth+1, total+players[i][depth])

#             visited[i] = 0 #다시 원래 상태로 되돌림 



# n = int(input().strip())
# players = []

# for _ in range(n):
#     max_ability = 0

#     for _ in range(11):
#         nums = tuple(map(int, input().split()))

#         if max_ability < max(nums): #선수들 중 최고 능력치
#             max_ability = max(nums)
#         players.append(nums)

#     max_total = 0

#     visited = [0 for _ in range(11)]

#     result = find_max_total(0, 0)
#     print(result)


# #s[i][j] = i번선수가 j번 포지션에서 뛸 때의 능력 

# # 능력치의 합의 최대값 

