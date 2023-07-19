# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
card_list = []
for _ in range(N):
    heappush(card_list, int(input()))

total = 0

while len(card_list) > 1:
    start_card = heappop(card_list)
    next_card = heappop(card_list)
    compare = start_card + next_card
    heappush(card_list, compare)
    total += compare

print(total)