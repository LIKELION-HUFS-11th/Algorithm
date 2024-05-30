
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]
l,r = min(budget), sum(budget) #예산중 최소에서 최대까지 왔다갔다 이동


while l <= r: #이분탐색
    m = (l+r)//2 #중간값. 인출할 금액임
    now = m #현재 가진돈.
    draw = 1 #인출 횟수

    for elem in budget: #예산 전부 돌기
        if now < elem: #가진 돈 부족하면 통장에서 인출
            now = m
            draw+=1
        now -= elem

# m번보다 더 많이 인출하거나 인출한 금액이 하루를 다 살기에 적은 경우 (인출 금액이 적음)
    if draw > M or m < max(budget): #M번 넘어가면.?
        l = m+1
    else:# 인출 횟수가 m번보다 적거나 같음 (인출 금액이 많음)
        r = m-1
        k = m
print(k)

#출처: https://yeoooo.github.io/algorithm/BOJ6236/