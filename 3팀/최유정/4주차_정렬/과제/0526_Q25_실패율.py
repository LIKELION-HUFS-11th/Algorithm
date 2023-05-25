# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    compare = []
    user = len(stages)
    clear_yet = [0] * (N+1)
    for s in stages:
        clear_yet[s-1] += 1

    for i in range(N):
        if clear_yet[i] == 0:
            compare.append([clear_yet[i], i+1])
        else:
            compare.append([clear_yet[i]/user, i+1])
            user -= clear_yet[i]

    compare.sort(key=lambda x: (-x[0], x[1]))

    for c in compare:
        answer.append(c[1])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))