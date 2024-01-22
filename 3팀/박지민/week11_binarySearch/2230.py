import sys






# import sys
# ## 입력
# n, min_limit = map(int, sys.stdin.readline().split()) # n :수의 개수, min_limit : 최소 차이
# array = []
# for _ in range(n):
#     array.append(int(sys.stdin.readline()))

# array.sort()

# start, end = 0, 0
# # 지금까지의 최소차이 (언제나 갱신되게)
# min_diff = sys.maxsize

# while start <= end and end < n:
#     take = abs(array[start] - array[end])

#     # 차이가 m 이상이고 
#     if take >= min_limit:
#         # 현재까지의 최소차이보다 작으면
#         if take < min_diff:
#             # 현재까지의 최소차이 갱신
#             min_diff = take
    
#     # 최소차이 m보다 차이가 작았다면 간격 넓히기: end
#     if take < min_limit: 
#         # 언제 시작점 조정
#         end += 1

#     # m보다 차이가 크다면, 간격 좁히기
#     if take > min_limit:
#         start += 1
# print(min_diff)


    
