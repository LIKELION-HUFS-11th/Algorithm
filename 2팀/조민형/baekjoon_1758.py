import sys

N = int(sys.stdin.readline())

people =[]
# 손님들이 생각하는 팁의 값 미리 받기
for i in range(N):
    tip = int(sys.stdin.readline())
    people.append(tip)

# 팁의 최댓값 -> 팁이 큰 사람의 순서대로 앞에 서 있으면 팁이 최대화됨
people.sort(reverse=True)
result = 0
#range를 len으로 설정해서 j를 등수로 활용
for j in range(len(people)):
    # 등수는 0등이 아닌 1등부터 시작하므로
    rank = j+1
    # 실질적으로 받는 팁 계산 -> 음수일경우 패스, 양수일 경우 결과에 더함
    if people[j] - (rank-1) < 0:
        pass
    else: result += people[j] - (rank-1)

print(result) 