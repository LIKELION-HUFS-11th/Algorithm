n = int(input())

visited = [False] * n
depth = 0
ans = [0] * n

def dfs(depth:int):
    if depth == n:
        print(*ans)
        return
    for i in range(n):
        print(depth, ans, i, visited)
        if not visited[i]:
            visited[i] = True
            ans[depth] = i+1
            print
            (depth, ans, i, visited)
            dfs(depth+1)
            visited[i] = False
            print(depth, ans, i, visited)

dfs(0)