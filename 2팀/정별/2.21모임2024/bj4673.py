# n은 d(n)의 생성자
# 원인이 되는게 없는 애들. 최초임.


def init(n): #셀프 넘버 구하는 함수 먼저
    ans = n
    while n != 0:
        ans += n%10
        n //= 10
    return ans

num = [0]*10001 #빈칸 만들기
for i in range(10001):
    a = init(i) #생성자 계산
    
    if a < 10001:
        num[a] += 1 #빈칸에 수 더하기
    #셀프넘버에서 제외디지 않은 애들임
    if num[i] == 0:
        print(i)