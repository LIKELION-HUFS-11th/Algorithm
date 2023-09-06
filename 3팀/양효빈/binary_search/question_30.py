def solution(words, queries):
    answer = []
    for query in queries:
        query_cnt = 0
        for word in words:
            n = len(word)
            if n == len(query):
                cnt = 0
                for i in range(n):
                    if query[i] == "?" or query[i] == word[i]:
                        cnt += 1
                if cnt == n: query_cnt += 1
        answer.append(query_cnt)
    return answer
## 



## 이진탐색 알고리즘
def binary_count(array, target):
    n = len(array)

    left = binary_left(array, target, 0, n-1)
    if left == None:
        return 0

    right = binary_right(array, target, 0, n-1)
    arr = [left, right]
    
    return arr



def binary_left(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if (mid == 0 or array[mid-1] < target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_left(array, target, mid+1, end)
    else:
        return binary_left(array, target, start, mid-1)



def binary_right(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] <= target:
        return binary_right(array, target, mid+1, end)
    else:
        return binary_right(array, target, start, mid-1)



def solution(words, queries):
    answer = []
    
    for query in queries:
        for word in words:
            cnt = 0
            if len(word) == len(query):
                arr = binary_count(query, "?")
                left_idx = arr[0]
                right_idx = arr[1]
                if (word[0:left_idx] == query[0:left_idx]) and (word[right_idx+1:] == query[right_idx+1:]):
                    cnt += 1
            answer.append(cnt)
            
    return answer






# def solution(words, queries):
#     answer = []
#     for query in queries:
#         query_cnt = 0
#         left_idx = query.find("?")
#         right_idx = query.rfind("?")
#         for word in words:
#             if 
#             if left_idx == 0:
#                 if word[right_idx+1 :] == query[right_idx+1:]:
#                     query_cnt += 1
#             elif word[0:left_idx] == query[0:left_idx]  and  word[right_idx+1:] == query[right_idx+1:]:
#                 query_cnt += 1
#             elif right_idx == len(word)
            
#         answer.append(query_cnt)
#     return answer






















