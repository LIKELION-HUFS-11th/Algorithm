# 입력
a = input()
b = input()

#d
# 교체를 먼저 하는 게 최소 연산 횟수인 것 같음
# 현재 위치에서 연산 최소 횟수 = d[i]

# 26을 1로 만들기 위한 연산 최소 횟수 = d[i]


# 사용할 수 있는 연산 방법
# 1) 삽입 2) 삭제 3) 교체

# 목표 문자열인 b의 길이만큼 
# d = [a] * len(b)
d = [0] * len(b)

#두 개의 길이가 같은 경우


# b를 만들기 위해 필요한 문자 찾기
for i in a:
    for j in b:
        if i == j:
            d.append(i)
        elif a.count(i) != d.count(i):
            d.remove(i)


for index_b in range(len(b)):
    for index_d in range(len(d)):
        if b[index_b] == d[index_d]:
            d[index_b:index_b+1] = b[index_b]
            d[index_d]:index_d+1 = 0

print(d)
    
            
# b에는 있는데, a에는 없는 문자 찾기
# 그럼 둘의 교집합부터 찾아야 함
# step1. s,u,d,a,a,y -> d에 저장

# step 2. b에서 d에 저장된 문자들의 위치를 확인 (0,1,3,5,6,7) -> 교체

# d 0 1 2 3 4 5 6 7
#   s a   u   d a y

# step 3. 2,4 자리에 삽입하면 됨 


# 0 1 2 3 4 5 6 7
# s u n d a y
# s a t u r d a y

# 0 0 0 0 0 0 0 0

# 1. n을 r로 교체
# 2. a 삽입
# 3. t 삽입


# r i in a:




# cat 
# cut 

# a를 b로 만들기 위해 



# 출력: 연산 횟수의 최솟값