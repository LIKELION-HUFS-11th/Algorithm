import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())  # 지원자 수
    people = []  # 지원자 정보 담을 리스트
    cnt = 0  # 신입사원 수

    for _ in range(n):
        person = list(map(int, input().split()))
        people.append(person)
    
    people = sorted(people)  # 신입사원 정보를 1차 서류심사 등수로 정렬
    highest = people[0][1]  # 지금까지 순회한 사람 중 가장 높은 2차 면접심사 등수

    '''
    [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    '''

    for i in range(1, n):  # 첫번째 사람은 무조건 합격이므로 index 1부터
        if people[i][1] < highest: 
            cnt += 1
            highest = people[i][1]


    print(cnt + 1)  # 아까 첫번째 사람은 무조건 합격이었어서 1 더하기