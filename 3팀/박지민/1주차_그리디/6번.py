from operator import itemgetter
def solution(food_times, k):

    foods = [] 
    n = len(food_times) 
    for i in range(n):
        foods.append((food_times[i], i+1)) #튜플 형태(첫 번째 값인 걸리는 시간 별로 sorting)
    foods.sort() #튜플 sorting할 때는 첫 번째 값을 먼저 비교해서 sorting
    pretime = 0 #이전 음식을 먹는 시간

    for i, food in enumerate(foods): #enumerate(): 튜플 생성
        diff = food[0] - pretime #diff=높이차, food[0]: 첫 번째 음식을 먹는 시간
        if diff != 0:
            spend = diff * n #쓴 시간=(높이차)*(남은 음식 수)
            if spend <= k: #근데 빼기 전에 뺄 수 있는지 먼저 확인하기
                k -= spend 
                pretime = food[0] 
            else:
                k %= n
                sublist = sorted(foods[i:],key=itemgetter(1)) #남은 음식=i번째 음식부터(원래 음식 번호로 재정렬, 튜플에서 1번 인덱스)
                return sublist[k][1] #몇 번째 음식인지(=i+1) 반환해줘야 하니까


        n -= 1 #턴 끝날 때마다 음식 하나를 처리한 거니까 n 빼주기

    return -1 