# 입력
n, m, l = map(int, input().split()) # n:현재 휴게소 수, m:더 지으려는 휴게소 수, l: 고속도로 길이
rest_list = list(map(int, input().split())) #현재 휴게소 있는 위치
## 구하려는 것: 휴게소 없는 구간의 길이의 최댓값
start, end = 1, l 

# 휴게소 위치 정렬
rest_list.sort()

# 더 지으려는 휴게소 수 = m
# 새로 생기는 휴게소 수 = cnt
# 휴게소 없는 구간 최대 길이 = length

length_list = []
# # 고속도로 시작-첫 휴게소 구간을 세고 있지 않다면
# if rest_list[0] != 1:
#     length_list.append(rest_list[0])
# # 마지막 휴게소 - 고속도로 끝 구간을 세고 있지 않다면
# elif rest_list[n-1] != l:
#     length_list.append(l - rest_list[n-1] + 1)

for i in range(1, n):
        # 고속도로 시작-첫 휴게소 구간을 세고 있지 않다면
    if i-1 == 0 and rest_list[i] != 1:
        length_list.append(rest_list[0])
    # 마지막 휴게소 - 고속도로 끝 구간을 세고 있지 않다면
    elif i == n-1 and rest_list[i] != l:
        length_list.append(l - rest_list[n-1] + 1)
    length = rest_list[i] - rest_list[i-1] + 1
    length_list.append(length)

# 최대 구간 찾기
# max_term = 0
# for i in range(len(length_list)):
#     if max_term < length_list[i]:
#         max_term_length = length_list[i]
#         max_term = i # 0번째 휴게소
# print(max_term_length, max_term)
# max_term = max(length_list)
# max_term_point = 0
# for max_term_point in range(len(length_list)):
#     if == max_term: 


# while start <= end:
#     mid = (start + end) // 2 
    
        
    #     cnt += 1   
    # if cnt >= m:
    #     ans = length 
    #     end = mid - 1
    # else:
    #     start = mid + 1