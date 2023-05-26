N = int(input())
a_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num, min_num = -float('inf'), float('inf')

def dfs(cnt, result, operator):
    global max_num, min_num

    if cnt == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    else:
        if operator[0]:
            operator[0] -= 1
            dfs(cnt+1, result+a_list[cnt], operator)
            operator[0] += 1
        if operator[1]:
            operator[1] -= 1
            dfs(cnt+1, result-a_list[cnt], operator)
            operator[1] += 1
        if operator[2]:
            operator[2] -= 1
            dfs(cnt+1, result*a_list[cnt], operator)
            operator[2] += 1
        if operator[3]:
            operator[3] -= 1
            dfs(cnt+1, int(result/a_list[cnt]), operator)
            operator[3] += 1

dfs(1, a_list[0], operator)
print(max_num)
print(min_num)
