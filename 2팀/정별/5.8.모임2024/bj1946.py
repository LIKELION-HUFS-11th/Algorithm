#그리디

import sys
        
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    arr.sort() #앞에 서류심사 기준으로 오름차순

    cnt =1 #이미 초깃값 사원 포함
    nMax = arr[0][1] #초깃값은 서류성적 가장 높은 사원의, 면접 성적임
    for i in range(1, N):
        
        if nMax > arr[i][1]: #이미 서류는 정렬되었으니, 면접으로만
            cnt += 1
            nMax = arr[i][1] #최댓값 정돈
        
    print(cnt)
