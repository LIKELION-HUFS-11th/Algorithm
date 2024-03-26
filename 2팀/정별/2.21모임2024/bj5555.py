target = input().strip()  # 찾고자 하는 문자열
n = int(input())          # 반지의 개수

count = 0  # 찾고자 하는 문자열을 포함하는 반지의 개수

for _ in range(n):
    ring = input().strip()  # 반지의 문자열 입력
    ring += ring  # 반지는 시작과 끝이 연결된 형태이므로, 문자열을 두 번 이어 붙임
    if target in ring:  # 찾고자 하는 문자열이 반지에 포함되어 있으면
        count += 1       # count 증가

print(count)
