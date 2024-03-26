import sys
input = sys.stdin.readline

n, l = map(int, input().split())

for length in range(l, 101):  # 가능한 짧은 길이인 l부터 최댓값인 100까지 순회
    sum = (length * (length - 1)) // 2  # 등차수열의 합 계산하기 (길이가 3이라면 1+2+3부터 계산해두기)
    leftover = n - sum  # 주어진 합 n에서 계산해둔 등차수열의 합 빼기
    # 남은 합이 0보다 작다면, 즉 계산해둔 등차수열의 합이 n보다 크다면 해당 length로 정답을 구할 수 없음
    # (길이가 3인데 1 2 3으로도 합이 넘어버리면 불가능 하니까)
    # 남은 합을 길이로 나눈 나머지가 0이 아니라면 (나누어떨어지지 않는다면) 해당 length로 정답을 구할 수 없음
    # (1 2 3에 각각 4씩 더한 5 6 7로 n을 만족해야 하는데 그럴 수 없으므로)
    if leftover >= 0 and leftover % length == 0: 
        start = leftover // length # 수열의 시작값
        ans = []  # 수열을 담을 리스트
        for i in range(length):
            ans.append(str(start + i))  # 길이만큼 수열 만들기
        print(' '.join(ans))  # 리스트를 공백과 함께 문자열로
        break
else:  # 모든 요소 순회 후에도 조건을 만족하는 경우가 없다면 (break를 만나지 못했다면)
    print(-1)
