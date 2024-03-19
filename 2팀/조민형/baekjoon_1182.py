import sys

N, S = map(int,sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))
result = 0

def subset(index, sum):
    global result
    
    # 부분수열의 index 받아서 N개만큼이면
    if index >= N:
        return
    # 부분수열에서 추가된 값 더하기
    sum += sequence[index]

    # 합이 S와 같다면 결과값에 1 추가
    if sum == S:
        result += 1

    #재귀 호출로 각 경우의 수 모두 구하기 (Brute force)
    # 해당 index를 선택했을 경우
    subset(index+1, sum)
    # 해당 index를 선택하지 않았을 경우
    subset(index+1, sum - sequence[index])

#시작점 호출
subset(0,0)
print(result)