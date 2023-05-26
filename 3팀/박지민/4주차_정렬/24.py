#입력
n = int(input())
house = list(map(int, input().split()))

#설계
#정렬부터
#위치한 집들만 고려해 이들의 중간값
#(n-1)//2 = 실수 인 경우는 고려 안 해도 되나..?
house.sort()

ant = (n-1) // 2 

#출력
print(house[ant])