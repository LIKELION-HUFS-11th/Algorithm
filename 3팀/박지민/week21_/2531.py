def max_sushi_varieties(sushi, N, k, c):
    cp1, cp2 = 0, k - 1
    check = set()

    while cp1 < N:
        if cp2 >= N:
            cp2 -= N
        if cp2 < cp1:
            plates = sushi[cp1:] + sushi[:cp2 + 1]
        else:
            plates = sushi[cp1:cp2 + 1]
        cases = set(plates)
        if c not in cases:
            cases.add(c)
        if len(check) < len(cases):
            check = cases
        cp1 += 1
        cp2 += 1

    return len(check)


N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

result = max_sushi_varieties(sushi, N, k, c)
print(result)

# ## 아이디어
# ## 변수
# n, d, k, c = tuple(map(int, input().split()))
# data = []
# for _ in range(n):
#     data.append(int(input()))

# max_type = 0 #최대 가짓 수
# interval_count = 0 
# interval_eaten = set()
# start = 0

# for end in range(n):
#     # 연속해서 4접시 먹는데 이미 먹은 종류이면 pass
#     while interval_count < k and end < n:
#         # 먹은 적이 없다면
#         if data[end] not in interval_eaten:
#             interval_eaten.add(data[end]) # 먹은 애 체크
#             interval_count += 1 # 먹은 종류 수 증가
#         end += 1
#             # max_type = max(max_type, len(eaten)) # 최대 가짓 수 갱신
#     # 연속해서 k접시 다 먹었으면
#     if interval_count == k:
#         # 먹은 리스트에서 쿠폰번호에 해당하는 게 없는 애들이 있다면 걔네 선택
#         if c in interval_eaten:
#             max_type = max(max_type, k+1)
#         else: 
#             max_type = max(max_type, k)

#         interval_eaten.remove(data[start])
#         interval_count -= 1
#         start += 1
#     end -= 1

# print(max_type)

