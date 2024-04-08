#알고리즘 교재 '동적계획 알고리즘'- '배낭문제' 참고
#배낭의 용량이 물건의 개수에 비해 매우 크면, 알고리즘 수행시간이 
    #너무 오래걸려 현실적으로 해를 찾을 수가 없다
import sys
n, k = map(int, sys.stdin.readline().split())

nItems = [[0, 0]] #후보지 물건들 담는 리스트

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    nItems.append([w, v])

# nItems.sort(key=lambda x: x[1]) #각 물건의 가치로 오름차순
nList = [[0 for _ in range(k+1)] for _ in range(n+1)]
#(i-1)할때 인덱스 에러날까봐 맨 앞에 빈 리스트 늘려준것

#한개의 열이 더해진 배낭 용량의 합임

for i in range(1, n+1): #부분 배낭 후보 도는 것임
    i_weight = nItems[i][0] #현재 고려중인 물건 i의 무게
    
    for w in range(1, k+1): #1에서 최대 용량까지, 최선의 배낭 가치 만들어가기

        if i_weight > w: #지금 후보지가 되는 물건이, 현재 임시 배낭 크기보다 크면
            nList[i][w] = nList[i-1][w]
        else:
            #새 물건을 배낭에 담지 않는 경우와/ 담는 경우 고려
            if nList[i-1][w-i_weight] + nItems[i][1] >= nList[i-1][w]:
               #담는 경우
                nList[i][w] = nList[i-1][w-i_weight]+nItems[i][1] 
            else: 
                nList[i][w] =  nList[i-1][w]

# print(nList)
print(nList[n][k])



# #처음에 그리디로 접근하다가 실패-> 얘는 부분배낭문제
# import sys
# n, k = map(int, sys.stdin.readline().split())

# nItems = []

# for _ in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     nItems.append([w, v])

# nItems.sort(key = lambda x: -x[1])

# nnBag = [] #현재 배낭에 담긴 물건 리스트
# nWeight = 0 #현재 배낭에 담긴 무게합
# nValue = 0 #현재 배낭에 담긴 물건들의 가치합
# print(nItems)

# res_val = 0 #가치합의 최댓값
# for elem in nItems:
#     if k >= (nWeight+elem[0]): #아직 전체 배낭 용량이 현재 무게+들어갈 무게보다 크다면
#         nnBag.append(elem)
#         nWeight += elem[0]
#         nValue += elem[1]
        
#         if k-nWeight >0:
            