import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
pays = list(map(int, input().split()))


profit = 0
for i in range(0, m):
    profit += pays[i]
max_profit = profit

start = 0
end = m - 1

while end < n - 1:
    end += 1
    profit -= pays[start]
    profit += pays[end]
    max_profit = max(max_profit, profit)
    start += 1

print(max_profit)