import sys

N = int(sys.stdin.readline())
color_loc = {}
for _ in range(N):
    loc, color = map(int,sys.stdin.readline().split())
    if color in color_loc:
        color_loc[color].append(loc)
    else: color_loc[color] = [loc]

result = 0
for i in color_loc:
    if len(color_loc[i]) == 2:
        result += (max(color_loc[i]) - min(color_loc[i])) * 2
    elif len(color_loc[i]) >=3:
        color_loc[i].sort()
        result += (color_loc[i][1]- color_loc[i][0]) + (color_loc[i][-1] - color_loc[i][-2])
        for j in range(1,len(color_loc[i])-1):
            if color_loc[i][j] - color_loc[i][j-1] > color_loc[i][j+1] - color_loc[i][j]:
                result += color_loc[i][j+1] - color_loc[i][j]
            else: result += color_loc[i][j] - color_loc[i][j-1]
print(result)
    
    

    
    
    