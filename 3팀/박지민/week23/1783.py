n, m = map(int, input().split())

max_visited = 0
# n이 1일 때 무조건 1
if n == 1:
  max_visited = 1
# n이 2일 때
elif n == 2: 
  if m >= 1 and m <= 6: # m이 1~6일 때
    max_visited = (m + 1) // 2 
  elif m >= 7: # 7이상일 때
    max_visited = 4
# n이 3 이상일 때
elif n >= 3: 
  if m <= 6: # m이 1~6일 때
    max_visited = min(m, 4)
  elif m >= 7: # m이 7 이상일 때
    max_visited = m - 2

print(max_visited)
