import sys
sString = input()
# print(len(list(sString)))

sAns = input()
# print(sList, sAns)
cnt = 0

idxMap ={}
for i, char in enumerate(sString): #고유값 매핑
    idxMap[char] = i+1
# print(idxMap)

L = len(list(sString))
for char in sAns: #암호 하나씩 돌기
    order = idxMap[char]
    cnt = (cnt* L + order) %900528
    #만약 첫번째 문자 해독한 후 문자열 전체 길이 곱함
        #두번째 문자 해독할 때 이전 문자열 영향을 현재 변환에 반영

print(cnt % 900528)