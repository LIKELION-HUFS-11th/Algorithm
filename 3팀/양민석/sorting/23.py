# n 입력
n = int(input())

# students 입력
students = []

for _ in range(n):
    name, kor, eng, math = input().split()
    students.append([name, int(kor), int(eng), int(math)])

# 설계
# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

# 출력
for student in students:
    print(student[0])