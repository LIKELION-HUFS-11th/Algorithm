#정아누나 아이디어

n, r, c = map(int, input().split())

'''
재귀 함수를 이용한 풀이

[메인 아이디어 겸 규칙]
1. (x * 2, y * 2)의 값 == 4 * (x, y)의 값 ((x, y)의 두 배에 해당하는 좌표의 값은 (x, y) 값의 네 배)
2. 제일 작은 z(2*2) 안에서 (x, y)의 방문 순서 == 2*(x%2) + y%2
'''

def rec(n, r, c): 
    if n == 0: #n 0될따ㅐ까지 하는 것임.
        return 0
    
    # 규칙 1을 이용해 (r, c)가 어디 출신인지 탐색
    # 1) n이 0이 될 때까지(최대 좌표가 (2**n-1, 2**n-1), 좌표를 1/2씩 위로 이동하면 최대 재귀 n-1번)
    # 2) (r, c)의 출신 좌표는 무조건 행과 열 좌표가 다 짝수(==제일 작은 z의 제일 첫번째)
    # 3) //를 함으로써 r이나 c가 홀수이면(==제일 작은 z의 제일 첫번째가 아니어도)
    # 제일 작은 z의 제일 첫번째로 만들어 줌
    from_num = rec(n-1, r//2, c//2)
    
    # 규칙 2를 통해 제일 작은 z에서의 방문 순서 구함
    z_idx = 2 * (r % 2) + (c % 2) #가장 작은 사각형에서, 위치.
    
    # (r, c)의 값 == (r, c)의 출신좌표의 값의 네 배 + 제일 작은 z에서의 방문 순서
    return 4 * from_num + z_idx

print(rec(n, r, c))






#구글링한 코드. 이해x

# #r행 c열을 몇번째로 방문하는지??
# import sys

# N, r, c = map(int, sys.stdin.readline())

# # 0 ≤ r, c < 2**N

# def z(n, r, c, res): #n r c res가 계속 움직임.
#     #계속 n-1하면서 
#     length = 2 ** n
#     half = length // 2  # 사분면으로 만들기위한 전체 배열길이의 절반 길이.

#     if n == 1: # 재귀 종료조건 2x2 4 최소 사분면이 만들어질 경우
#         print(2 * r + c + res)  # row가 늘어나면 도착횟수가 2씩 늘어나고 colunm이 늘어나면 1씩 늘어난다.
#         return

#     if r >= half and c >= half:  # 4사분면일때
#         z(n - 1, r - half, c - half, res + 3 * half * half)
        
#     elif r >= half > c:  # 3사분면일때
#         z(n - 1, r - half, c, res + 2 * half * half)
#     elif r < half <= c:  # 2사분면일때
#         z(n - 1, r, c - half, res + half * half)
#     else:  # 1사분면일때
#         z(n - 1, r, c, res)

# z(N, r, c, 0)
