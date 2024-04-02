import sys
import heapq
n = int(sys.stdin.readline())
timetable = []
for _ in range(n):
    timetable.append(list(map(int, sys.stdin.readline().split())))
    
timetable.sort(key=lambda x:(x[0],x[1]))

time = [timetable[0][1]]
for i in range(1,n):
    if time[0] <= timetable[i][0]:
        heapq.heappop(time)
    heapq.heappush(time,timetable[i][1])
print(len(time))