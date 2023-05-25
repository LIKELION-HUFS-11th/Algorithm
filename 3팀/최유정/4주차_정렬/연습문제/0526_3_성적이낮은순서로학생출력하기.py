N = int(input())
score_list = [input().split() for _ in range(N)]
score_list.sort(key=lambda x:x[1])

for score in score_list:
    print(score[0], end=" ")