import sys
from collections import defaultdict, deque

n = int(input())
n1, n2 = map(int, sys.stdin.readline().split())

m  = int(input())
nList = defaultdict(list) #value 자리를 리스트로 받기위해. append 사용하기 쉬움.
for _ in range(m):
    x, y = map(int, input().split())
    nList[x].append(y)  #부모 -> 자식 관계
    nList[y].append(x)  #자식 -> 부모 관계. 양방향으로 탐색
# print(nList)

def bfs(start, target):
    visited = {start}# 방문여부. set형태.
    
    queue = deque([(start, 0)])  #(현재 노드, 현재까지의 촌수)
    
    while queue:
        current, cnt = queue.popleft()
        if current == target: #현재 노드가 처음에 계획한 노드까지 왔다면
            return cnt
        
        for elem in nList[current]: #nList에서 현재 위치한 노드.와 연결된 모든 애들 다 도는것임.->bfs
            if elem not in visited: #방문한 얘가 아니라면.
                visited.add(elem)
                queue.append((elem, cnt + 1))
            #q방문했다면 Pass
    return -1

print(bfs(n1, n2))



# nDict = {}
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     if x in nDict :
#         nDict[x].append(y) #요소 추가
#         nDict[y].append(x)
#     if y in nDict:
#         nDict[x].append(y) #요소 추가
#         nDict[y].append(x)
#     else:
#         nDict[x] = [y] #이렇게 추가해야 append에서 에러 안걸림
#         nDict[y] = [x]

# nList = sorted(nDict.items()) #정렬과 동시에 리스트로 변신
# print(nList)

# n1Box =[]
# n2Box = []
# for idx, elem in enumerate(nList):
#     if n1Box and n2Box: break
    
#     if n1 in elem[1]: #누군가의 자식이라면, 그 관계 자체 전부 가져오기
#         n1Box.append([idx, elem])
#     elif n2 in elem[1]:
#         n2Box.append([idx, elem])
# n1Box =n1Box[0]
# n2Box = n2Box[0]

# cnt=0
# while True:
#     if n1Box[1] == n2Box[1]:
#         print(cnt) #형제관계
#         break
#     elif n1 == n2Box[1][0] or n2 == n1Box[1][0]:
#         print(cnt+1) #부모관계
#         break
#     else:
#         pnt = n1Box[0] #n1의 자식으로서 인덱스 위치

#         if n1Box == n2Box: break
        
#         for idx, elem in enumerate(nList):
#             if n1Box[1][0] in elem[1]: #n1의 부모
#                 pnt = idx
#                 n1Box = [idx, elem] #n1Box 리셋
#                 cnt+=1
#                 break
    
            




