N = int(input())

if N <= 99:
    cnt = N
else:
    cnt = 99 #정답
    idx = 99
    while idx < N:
        idx+=1
        nF = idx // 100 #첫째자리수
        nS = (idx % 100) // 10 #둘째자리수
        nT = idx % 10 #셋째자리수

        if (nF - nS) == (nS - nT):
            cnt += 1
print(cnt)