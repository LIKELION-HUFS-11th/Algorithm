#못풀음
n = int(input())
#싸이클 유무.
nGrapgh = []
for i in range(n):
    b = int(input())
    nGrapgh.append([i, b-1]) #1,2번째 줄 묶어서 만든 배열
nVisited = [0 for _ in range(n)]
nAns = []

def dfs(x, visit):#visit은 리스트
    if not visit[x]: #방문안했으면 방문표시
        visit[x]=1
    else:#방문한 곳에 돌아왔으면 싸이클을 다 돈것임
        nAns.append(tuple(set(nGrapgh[x]))) #[2,0]과 [0,2]는 동일함. set으로 중복제거
        return
    

# nEmpty = [0 for _ in range(n+1)]
# nKeys = []
# nValues = []
# for idx, zero in enumerate(nEmpty):
#     if idx == 0: #1부터 시작
#         continue
#     nKeys.append(idx)
#     nValues.append(int(input()))
# # print(nKeys, nValues)
# # dp = [0 for _ in range(n+1)]

# # for i in range(1, n+1):
    
# #     if set(nKeys[:i+1]) = =set(nValues[:i+1])


    