import sys
nTotal = int(input())

def cnt_combinations(strCl):
    cnt = {}
    for cl, kind in strCl:
        cnt[kind] = cnt.get(kind, 0) +1
    
    combination = 1
    for elem in cnt.values():
        combination *= (elem +1)
    
    return combination - 1

ans = [] #answer
for _ in range(nTotal):
    nNums = int(input())
    strCl = []
    for i in range(nNums):
        x, y = sys.stdin.readline().split()
        # if y not in dic:
        #   dic[y] += 1
        strCl.append((x,y))
    ans.append(cnt_combinations(strCl))
    
for elem in ans:
    print(elem)
            

    