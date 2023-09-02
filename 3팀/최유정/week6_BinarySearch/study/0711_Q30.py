# 가사 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

# 1. word는 길이별로 딕셔너리에 저장
# 2. queries를 돌면서 길이랑 ?로만 이루어져있는지 확인
# 2-1. query의 길이 저장
# 2-2. 만약 해당 길이를 가진 word가 없을 경우 append(0)
# 2-3. query가 ?로만 이루어졌다면 해당 길이랑 똑같은 word 개수 카운트해서 append
# 3. 위의 경우에 해당이 안된다면, ?로 시작하는 query인지 아닌지 확인
# 3-1. ?로 시작하면 ?가 끝나는 위치를 이진탐색으로 통해 찾기
# 3-2. ?로 끝나면 ?가 시작하는 위치를 이진탐색으로 찾기
# 4. 각각 찾은 위치를 토대로 같은 길이를 가진 word 리스트를 돌면서 같은 단어를 가진 word있으면 카운트해서 append
# 4-1. ? 시작 위치 : 0~(? 위치 바로 앞)
# 4-2. ? 끝 위치 : (? 위치 바로 뒤)~마지막 인덱스


# 물음표가 중간부터 끝까지 있을 때 (물음표 시작 위치 찾기)
def find_mark_right(query, start, end):
    if start > end:
        return mid
    mid = (start + end) // 2
    if query[mid] != "?":
        return find_mark_right(query, mid+1, end)
    elif query[mid] == "?" and query[mid-1] =="?":
        return find_mark_right(query, start, mid-1)
    else:
        return mid

# 물음표가 시작부터 중간까지 있을 때 (물음표 끝 위치 찾기)
def find_mark_left(query, start, end):
    if start > end:
        return mid
    mid = (start + end) // 2
    if query[mid] != "?":
        return find_mark_left(query, start, mid-1)
    elif query[mid] == "?" and query[mid+1] =="?":
        return find_mark_left(query, mid+1, end)
    else:
        return mid

# fro??
def is_same_s(words, q, start_mark):
    cnt = 0
    query = q[:start_mark]
    for w in words:
        if w[:start_mark] == query:
            cnt += 1
    return cnt

#????o
def is_same_e(words, q, end_mark):
    cnt = 0
    query = q[end_mark+1:]
    for w in words:
        if w[end_mark+1:] == query:
            cnt += 1
    return cnt

def solution(words, queries):
    answer = []
    words_dic = {}

    for w in words:
        l = len(w)
        if (l in words_dic):
            words_dic[l].append(w)
        else:
            words_dic[l] = [w]

    for q in queries:
        l = len(q)
        if l not in words_dic:
            answer.append(0)
            continue
        elif set(q) == {'?'}:
            answer.append(len(words_dic[l]))
        elif q[0] != "?":
            start_mark = find_mark_right(q, 0, l)
            answer.append(is_same_s(words_dic[l], q, start_mark))
        else:
            end_mark = find_mark_left(q, 0, l)
            answer.append(is_same_e(words_dic[l], q, end_mark))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))