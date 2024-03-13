import sys

N, L = map(int, input().split()) 
pos = 0 # 현재 이동 위치
answer = 0 

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos) # 현재위치에서 신호등위치까지 이동한것임
    pos = d # 현재 위치 갱신

    if answer % (r + g) <= r: # 경과시간 % (빨간불 + 초록불)이 빨간불 이하면 대기
        answer += (r - (answer % (r + g))) # 대기시간 더하기

answer += (L - pos) # 반복문을 돌고나면 나머지 신호등이 없는 도로의 길이.
print(answer)



# import sys
# n, l = map(int, sys.stdin.readline().split())


# blinker = [[0]]*(l+1)

# for i in range(n):
#     d, r, g = map(int, sys.stdin.readline().split())
#     blinker[d] = [d,r,g]
# print(blinker)


# t=1 #시간
# nLoc = 1 #현재 위치
# while t<= l:
    
#     if blinker[nLoc][0] == nLoc: #해당 위치에 차가 도달했을 때
#     #초록이면 pass, 빨강이면 stop+바뀔 때까지 기다리기
#         if t <= r or t % (r+g) >g: #빨강불 조건
#             t+=1
#             continue
    
#     nLoc+=1
#     t+=1

# print(t)

