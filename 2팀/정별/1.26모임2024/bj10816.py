#처음에 접근한 풀이
#투 포인터로 while문에 재귀 활용
#시간초과

# nTotal_nums = int(input())
# nTotal = list(map(int, input().split()))
# nSang_nums = int(input())
# nSang = list(map(int, input().split()))

# def count_match(nSang, nTotal, nSstart, nTleft, nTright, nAns):
#     if nSstart == len(nAns):
#         return nAns
#     else:
#         nTleft = 0
#         nTright = len(nTotal) - 1
#         while nTleft < nTright:

#             if nSang[nSstart] == nTotal[nTleft]:
#                 nAns[nSstart] += 1
#                 nTleft += 1
#             else:
#                 nTleft += 1

#             if nSang[nSstart] == nTotal[nTright]:
#                 nAns[nSstart] += 1
#                 nTright -= 1
#             else:
#                 nTright -= 1
#         return count_match(nSang, nTotal, nSstart+1, nTleft, nTright, nAns)


# nTleft = 0
# nTright = nTotal_nums - 1
# nSstart = 0

# nAns = [0] * nSang_nums

# result = count_match(nSang, nTotal, nSstart, nTleft, nTright, nAns)
# print(result)


#두번째로 접근함
#for문 2개로 812ms

nTotal_nums = int(input())
nTotal = list(map(int, input().split()))
nSang_nums = int(input())
nSang = list(map(int, input().split()))

def count_match(nSang, nTotal):
    nAns = [0] * len(nSang)
    
    nTotal_dict = {}  # 각 값이 몇 번 나타나는지 저장

    # nTotal 의 각 요소들이, 딕셔너리의 key로 들어감. value에다가 한개라도 있으면 1 저장.
    #동일한 키값이면 거기다 1 또 더하는 것임
    for value in nTotal:
        nTotal_dict[value] = nTotal_dict.get(value, 0) + 1
    # print(nTotal_dict)
    # nSang 배열 기준으로, 각 값에 대해 딕셔너리에서 값을 찾아 nAns 업데이트
    for i, value in enumerate(nSang):
        nAns[i] = nTotal_dict.get(value, 0)

    return nAns

result = count_match(nSang, nTotal)

for elem in result:
    print(elem, end = ' ')
