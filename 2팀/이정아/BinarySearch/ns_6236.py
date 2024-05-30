import sys
input = sys.stdin.readline

n, m = map(int, input().split())
budgets = []
for _ in range(n):
    budget = int(input())
    budgets.append(budget)
left = min(budgets)
right = sum(budgets)



