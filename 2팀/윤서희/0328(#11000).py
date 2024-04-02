# import sys
# input = sys.stdin.readline

# n = int(input())
# times = []
# rooms = []

# for i in range(n):
#     time = list(map(int, input().split()))
#     times.append(time)
# times = sorted(times, key = lambda x: x[0])

# for time in times:
#     if len(rooms) > 0:
#         for i in range(len(rooms)):
#             if  rooms[i] <= time[0]:
#                 rooms[i] = time[1]
#                 break
#         else: rooms.append(time[1])
#     elif len(rooms) == 0:
#         rooms.append(time[1])        

# print(len(rooms))

import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = []
rooms = []

for i in range(n):
    time = list(map(int, input().split()))
    times.append(time)
times = sorted(times, key = lambda x: (x[0], x[1]))

rooms.append(times[0][1])

for i in range(1, n):
    if rooms[0] <= times[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, times[i][1])         

print(len(rooms))
