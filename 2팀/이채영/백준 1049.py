MAX_N, MAX_PRICE = 100, 1000

N, M = tuple(map(int, input().split()))

min_price_package, min_price_item = MAX_PRICE + 1, MAX_PRICE + 1

for _ in range(M):
    price_package, price_item = tuple(map(int, input().split()))
    min_price_package = min(min_price_package, price_package)
    min_price_item = min(min_price_item, price_item)

total = 0
if min_price_item * 6 < min_price_package:
    total = min_price_item * N

else: #패키지 +낱개 혼합 or 패키지 단독 가능
    cnt_package = N // 6 
    cnt_item = N % 6 
    total += cnt_package * min_price_package

    # print(total)
    
    #남은 N%6(<6)개의 줄 처리
    if min_price_item * cnt_item <= min_price_package:
        total += min_price_item * cnt_item
    else:
        total += min_price_package
    # print(total)

print(total)




#     if N % 6 == 0:
#         cost_package = price_package * (N // 6)
#     else:
#         cost_package = price_package * ((N // 6) + 1)

#     if N > 6 and N % 6 != 0: #패키지 +낱개 혼합 가능
#         cnt_package = N // 6 # 1
#         cnt_item = N % 6 #4
#         cost_package_and_item = (price_package * cnt_package) + (price_item * cnt_item)
#     else:
#         cost_package_and_item = (MAX_N + 1) * (MAX_PRICE + 1)
    
#     cost_item = price_item * N

#     print(cost_package, cost_package_and_item, cost_item)
#     min_cost = min(min_cost, cost_package, cost_item, cost_package_and_item)

#     # print(f"패키지 가격 {cost_package} 낱개 가격 {cost_item}")

# print(min_cost)

# #가능한 경우
# # 패키지만으로 (잉여가 생기더라도)
# # 패키지 + 낱개 (패키지 최대 + 남는 거 낱게)
# # 낱개만으로
# # 브랜드 간 교차 구매 가능