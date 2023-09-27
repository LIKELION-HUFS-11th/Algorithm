import sys
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited_alpha[ord(alpha_list[nx][ny])-65]:
            visited_alpha[ord(alpha_list[nx][ny])-65] = 1
            dfs(nx, ny, cnt+1)
            visited_alpha[ord(alpha_list[nx][ny])-65] = 0
    return result

R, C = map(int, input().split())
alpha_list = []
visited_alpha = [0]*26
for _ in range(R):
    alpha = list(input())
    alpha_list.append(alpha)
visited_alpha[ord(alpha_list[0][0])-65] = 1
result = 0
print(dfs(0, 0, 1))