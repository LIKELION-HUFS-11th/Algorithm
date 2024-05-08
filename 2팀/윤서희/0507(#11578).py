import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 문제 수, 학생 수
infos = [0b0000000000] * (m + 1)  # 이진수로 정보 저장할 리스트

for i in range(1, m + 1):
    a = list(map(int, input().split()))
    b = a[1:]  # O를 제외한 문제의 번호 P만 저장
    for j in b:
        infos[i] = infos[i] | (1 << j)  # 문제의 번호마다 이진수로 저장

for i in range(1, m + 1):
    tmp = set()  # 임시 집합 : 모든 가능한 정보의 경우의 수 저장
    for j in range(len(infos)):
        if infos[j] == 2 ** (n + 1) - 2:  # 모든 비트가 1이라면 : 모든 문제를 풀 수 있는 상태라면
            print(i)
            exit()  # 코드 종료
        for k in range(j + 1, len(infos)):
            tmp.add(infos[j] | infos[k])  # OR 연산
    infos = list(tmp)

print(-1)  # 아직도 코드가 종료되지 않았으면 : 풀 수 없으므로 -1 출력