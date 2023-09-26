'''
[회의실 배정]
https://www.acmicpc.net/problem/1931
'''
n = int(input())
classes = []
for _ in range(n):
    classes.append(tuple(map(int, input().split())))

classes.sort(key=lambda x : (x[1], x[0]))   # (1, 2) (2, 2)를 둘 다 선택하려면 x[1], x[0] 순서대로 정렬해야 함 

cnt = 1
prev_end = classes[0][1]
for i in range(1, n):
    if prev_end <= classes[i][0]:
        prev_end = classes[i][1]
        cnt += 1

print(cnt)