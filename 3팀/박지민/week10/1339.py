## 아이디어: 자릿수 위치가 높은 알파벳일수록, 더 큰 수를 할당한다 -> A는 만의 자리니까 제일 큰 9 할당

## Step 1. 자릿수 위치가 가장 높은 알파벳 찾기 
## alpha = [GCF, ACDEB] 
# ->  A:만의 자리, C: 천의 자리, G/C: 백의 자리.. 니까 A에는 만, C에는 천, G/C에는 백을 할당(근데 C는 나중에 천을 더 더해줘야 함)
# -> 각 알파벳에 해당하는 수를 내림차순해서 자릿수 위치가 가장 높은 알파벳 찾기
## Step 2. 알파벳 별 숫자 할당

import sys
## 입력
n = int(sys.stdin.readline()) #단어 수

alpha = [] # 단어들 저장할 리스트
alpha_dict = {} # 단어 내 알파벳에 해당하는 수 저장할 딕셔너리 -> {A:10000, C:1000..., 알파벳:알파벳에 해당하는 수}
numList = [] # 수 저장할 리스트

# 단어 입력받기
for _ in range(n): # 단어 수만큼
    alpha.append(sys.stdin.readline().rstrip())

## 알파벳에 해당하는 수를 할당 
for i in range(n): #모든 단어에 대해
    for j in range(len(alpha[i])): #단어의 길이만큼
        if alpha[i][j] in alpha_dict: # 그 알파벳이 딕셔너리에 있다면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
        else:                         # 없다면 해당하는 수를 만들어주기
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

# 숫자 리스트에 숫자들만 넣어주기
for val in alpha_dict.values():
    numList.append(val)

# 가장 자릿수가 큰 걸 찾기 위해 내림차순 정렬
numList.sort(reverse=True)

# 합 구하기
sum = 0 
special = 9 # 각 알파벳이 가질 고유 값
for num in numList:
    sum += num * special
    special -= 1

print(sum)