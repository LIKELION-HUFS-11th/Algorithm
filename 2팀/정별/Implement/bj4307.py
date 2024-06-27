#참고링크: https://fre2-dom.tistory.com/381
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    l, nums = map(int, input().split())
    nPos =[] #개미들 위치
    for _ in range(nums):
        nPos.append(int(input()))
    f_ant = 0 #가장 빠른시간
    l_ant =0 #가장 늦은시간
# print(nPos)
    for i in nPos:
            if i > l - i:
            # 가장 빠른 시간에 떨어질 경우
                if f_ant < l - i:
                    f_ant = l - i

                # 가장 늦은 시간에 떨어질 경우
                if l_ant < i:
                    l_ant = i

        # 개미의 위치가 막대의 좌측에 있다면
            else:
                if f_ant < i:
                    f_ant = i

                if l_ant < l - i:
                    l_ant = l - i

    print(f_ant, l_ant)