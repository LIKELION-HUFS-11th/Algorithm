#입력

# 식량창고의 개수 n
n = int(input())

# 식량창고에 저장된 식량 개수 K 
arr = list(map(int, input().split()))

# 최댓값을 저장할 리스트
d = [0] * 100

# 식량창고 0 1 2 3
# 식량개수 1 3 1 5

# 식량창고 0 1 2 3 4 5 6 7 
# 식량개수 1 3 1 5 1 3 1 5


d[0] = arr[0]
d[1] = max(arr[1], arr[0])
for i in range(2, n):
    # i 털지 말지 결정
    # d[i-1] > 현재 식량 개수 + d[i-2] -> d[i]는 어차피 대체됨
    # d[i-1] < 현재 식량 개수 + d[i-2] -> i 털기 
    d[i] = max(d[i-1], d[i-2]+arr[i])
    
# 출력
print(d[n-1])
