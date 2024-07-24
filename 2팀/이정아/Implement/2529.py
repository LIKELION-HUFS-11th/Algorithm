k = int(input())
signs = list(input().split())

visited = [False] * 10
max_ans, min_ans = "", ""

def is_possible(i:int, j:int, k:str):
    if k == ">":
        return i > j
    else:
        return i < j
    
def solve(cnt:int, s:str):
    global max_ans, min_ans
    
    if cnt == k+1:
        if not min_ans:
            min_ans = s
        else:
            max_ans = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or is_possible(s[-1], str(i), signs[cnt-1]):
                visited[i] = True
                solve(cnt+1, s+str(i))
                visited[i] = False

solve(0, "")
print(max_ans)
print(min_ans)