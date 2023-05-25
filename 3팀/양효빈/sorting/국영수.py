# 입력
n = int(input())
student_arr = [ list(input().split()) for _ in range(n)]

### 계수정렬


# 점수를 모두 정수로 바꾸기
for s in student_arr:
    s[1] = int(s[1])
    s[2] = int(s[2])
    s[3] = int(s[3])

# 빈 중첩리스트 생성
sort_arr = [[] for _ in range(101)] # sort_arr = [[]] * 101 과 차이..?


# 국어 점수에 따라 정렬(감소하는 순서)
for student in student_arr:
    korean = student[1]
    sort_arr[100-korean].append(student)

# 수학 정렬 함수
def math_sort(student):
    n = len(student)

    for _ in range(n):
        for i in range(0, n-1):
            if student[i+1][2] == student[i][2]:
                if student[i+1][3] > student[i][3]:
                    student[i+1][3], student[i][3] = student[i][3], student[i+1][3]
    return student



# 이름 정렬 함수
def name_sort(student):
    n = len(student)

    for _ in range(n):
        for i in range(0, n-1):
            if student[i+1][3] == student[i][3] and student[i+1][2] == student[i][2]:
                if student[i+1][0] < student[i][0]:
                    student[i+1][0], student[i][0] = student[i][0], student[i+1][0]
    return student
    


# 영어 점수에 따라 정렬(증가하는 순서)
for student in sort_arr:
    idx = sort_arr.index(student)
    if len(student) > 1:
        student.sort(key=lambda x: x[1])
        student = math_sort(student)
        student = name_sort(student)
    
        sort_arr[idx] = student


for student in sort_arr:
    if student != []:
        for s in student:
            print(s[0])




###














