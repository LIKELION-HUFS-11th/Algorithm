import sys
from collections import Counter

K, L = map(int, sys.stdin.readline().split())

student_list = []
for _ in range(L):
    student_list.append(sys.stdin.readline().rstrip('\n'))

counted_list = Counter(student_list)

student= 0
count = 0
while count != K and student<len(student_list):
    if counted_list[student_list[student]] > 1:
        counted_list[student_list[student]] -=1
    else:
        print(student_list[student])
        count +=1
    student+=1
