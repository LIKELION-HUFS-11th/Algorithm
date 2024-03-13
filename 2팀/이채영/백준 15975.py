import sys
input = sys.stdin.readline

n = int(input().strip())

blank = dict() #{색깔 : 좌표}로 저장 -> 같은 색인 좌표들끼리만 비교하면 되기 때문!


for _ in range(n):
    point, color = map(int, input().split())

    if color in blank.keys():
        blank[color].append(point)
    else:
        blank[color] = [point]


total_len = 0
for c in blank.keys(): # {색깔 : [좌표1, 좌표2...]}
    blank[c].sort()

    for i in range(len(blank[c])): #매번 점들에서 가까운 길이 저장
        points = blank[c]

        if len(points) == 1:
            continue
        
        elif i == 0:
            len_arrow = points[i+1] - points[i]
        
        elif i == len(points) - 1:
            len_arrow = points[i] - points[i-1]

        else:
            len_arrow = min(points[i+1]-points[i], points[i]-points[i-1])

        total_len += len_arrow

print(total_len)