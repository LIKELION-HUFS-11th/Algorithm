from collections import deque
n = int (input( ))
m = int (input( ))
graph = [[]  for _ in range (n+1)]
for _ in range (m):
    a, b = map(int, input () .split())
    graph[a].append(b)
    graph [b].append(a)
    

que = deque()
que.append((1, 0))

visited = [0 for _ in range (n+1)]
visited [1] = 1
answer = 0

while que:
    x, cnt = que.popleft ( )
    if cnt >=2:
        continue
    for friend in graph[x]:
        if visited[friend]==0:
            visited[friend] = 1
            que.append((friend, cnt+1))
            answer += 1
print (answer)




# import sys

# n= int(input())
# m= int(input())

# nAns = [0] *(n+1) #최정적으로 결혼식 데려갈 친구들
# nFriends=[] #상근이 직접 친구들
# nOthers=[]  #일단 상근이 직접 친구 아닌애들

# for i in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     if x == 1:
#         nFriends.append(y) 
#         nAns[y]+=1 #직접 친구들은 데려가기 확정
#     else:
#         nOthers.append([x, y])
# nOthers = sorted(nOthers, key = lambda x : x[0])

# for elem in nOthers: #조건 맞는 후보지들만 추리기
#     if elem[0] not in nFriends:
#         if elem in nOthers:
#             nOthers.remove(elem)


# if not nFriends: #상근이 직접 친구 아무도 없을 때
#     print(0)
# elif not nOthers: #상근이 직접 친구만 있고, 간접 친구 없을 때
#     cnt=0               
#     for elem in nAns:
#         if elem:
#             cnt+=1
#     print(cnt)

# else:
#     for direct in nFriends: #직접 친구들
#         for indirect in nOthers: #간접 친구들
#             if direct == indirect[0]:
#                 nAns[indirect[1]] += 1 #간접 친구 데려가기 확정
    
#     cnt=0               
#     for elem in nAns:
#         if elem:
#             cnt+=1
#     print(cnt)
    
 

# # print(nAns)
