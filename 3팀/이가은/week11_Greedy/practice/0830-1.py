n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

'''
* 시간복잡도 : O(K_화폐의 종류)
    - 시간복잡도는 동전의 총 종류에만 영향을 받고, 거슬러 줘야 하는 금액의 크기와는 무관
'''