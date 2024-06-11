#참고 링크: https://w00ye0l.tistory.com/67

#방법1: 거듭 제곱에서의 나머지 분배법칙 활용
def solution(a, b, c):
    if b == 1:
        return a%c
    
    tmp = solution(a, b // 2, c)

    if b%2 == 1: #b가 홀수면
        return ((tmp * tmp) % c) * a % c
    else:
        return (tmp * tmp) %c
    
a, b, c = map(int, input().split())

print(solution(a, b, c))

#방법2: 파이썬 내장함수 pow()활용
#pow(a, b, mode=None) 은 a의 b 거듭제곱 반환
#mod가 참이면(값이 있다면) 나머지 반환

# print(pow(a, b, c))

#방법3. 직접 곱하기
# # 제곱 쓰면 시간초과 나옴
# #에라토스테네스의 체 원리 고려해보자 ->메모리 초과
# #집합 고려해보자 -> 시간 초과
#     #애초에 큰 수 곱셈 자체가 시간 초과다

# import sys
# input = sys.stdin.readline()
# a, b, c = map(int, input.split())

# if a % c == 0: #a가 c의 배수라면
#     print(0)
# #규칙 찾기
# else:
#     idx = 1 #a의 지수. 최대 b까지 증가
#     nSum = a #a의 idx제곱만큼 곱한 값의 결과
#     nRest = [] #nSum을 c로 나눴을 때 생기는 나머지들을 보관할 리스트
#     # nVisited = [0 ] *c #메모리 초과..?

#     nVisited= set([0]) #집합
    
#     while idx <= b:
#         nLenVisit = len(nVisited)
#         #규칙성 있으면 반복문 탈출
        
#         if a<c: #idx 먼저 더함. 첫번째 나머지가 무조건 0임
#             idx += 1 #idx가 2부터 시작
#             if idx > b: break
            
#             nSum *= a
            
#             nNewrest = nSum %c 
#             nRest.append(nNewrest)
#             # nVisited[nNewrest] += 1
#             nVisited.add(nNewrest)
            
#         else: #a=c는 어차피 line8의 if문에 걸림
#             nNewrest = nSum %c
#             nRest.append(nNewrest)
            
#             idx+=1
#             nSum *= a
#             # nVisited[nNewrest] += 1
#             nVisited.add(nNewrest)
        
#         if nLenVisit == len(nVisited):#같은게 추가됐다면 길이가 유지됨
#             nRest.pop()
#             break
        
#         # if nVisited[nNewrest] == 2:
#         #     nRest.pop()
#         #     break
#     # print(nRest)#반복되는 규칙 찾음
#     # print(nRest)
#     # print(nVisited)
    
# #몇번째인지 확인
#     if len(nRest) > b:
#         print(nRest[b-1])
#     elif len(nRest) == b:
#         print(nRest[-1])
#     else: #len(nRest) <b
#         print(nRest[b % len(nRest) -1])