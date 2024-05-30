import sys

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h: #종료조건
        break

    nList = []
    
    for _ in range(h):
        
        nList.append(list(map(int, sys.stdin.readline().split())))
    # print(nList)
    
    


