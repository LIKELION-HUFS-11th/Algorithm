# https://www.acmicpc.net/problem/10825
# 국어 높은 점수부터, 영어 낮은 점수부터, 수학 높은 점수부터
import sys
input = sys.stdin.readline

N = int(input())
report_card = []
for _ in range(N):
    student, korean, english, math = input().split()
    report_card.append([student, int(korean), int(english), int(math)])

report_card.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for report in report_card:
    print(report[0])