import sys
input = sys.stdin.readline

# 시간초과 

n = int(input().strip())
lessons = []

for _ in range(n):
    l = tuple(map(int, input().split()))
    lessons.append(l)

#가장 빨리 끝나는 강의부터 배치한다
lessons.sort(key = lambda x: (x[1], x[0]))

"""
sol1
"""
classrooms = [] 
classrooms.append([lessons.pop(0)])
cnt = 1

i = 0
while lessons:
    new_s, new_t = lessons[i]

    satisfied = False
    for classroom in classrooms:
        s, t = classroom[-1]
        if new_s >= t:
            classroom.append(lessons.pop(i))
            satisfied = True
            break

    if satisfied == False:
        classrooms.append([lessons.pop(i)])
        cnt += 1

print(cnt)
    
"""
sol2 - 왜 힙을 써야하는지 잘 이해가안됨
"""
import heapq

classroom = []
heapq.heappush(classroom, lessons[0][1])

for i in range(1, n):
    if lessons[i][0] < classroom[0]: #새 회의실 개설
        heapq.heqppush(classroom, lessons[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, lessons[i][1])