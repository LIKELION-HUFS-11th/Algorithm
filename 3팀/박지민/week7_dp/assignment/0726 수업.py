# 클래스 선언
class Number:
    def __init__(self, element, index):
        self.element, self.index = element, index

#변수 선언 및 입력
# 수열의 길이
n = int(input()) 

# 수열을 오름차순 정렬했을 때 위치가 어느 위치로 이동하는지 출력

elements = []
for i in range(1, n+1):                       #     0 1 2 3 4 5 6
    element = list(map(int, input().split())) #전: [3 1 6 2 7 30 1]
elements.append(Number(element[i-1], i))

# 정렬                                              0 1 2 3 4 5 6 
elements.sort(key=lambda x: x.element)        #후: [1 1 2 3 6 7 30]

#출력
print(elements)