import sys
import heapq

input = sys.stdin.readline

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(input().strip())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)