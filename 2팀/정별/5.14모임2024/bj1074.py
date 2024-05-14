#이해x

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
