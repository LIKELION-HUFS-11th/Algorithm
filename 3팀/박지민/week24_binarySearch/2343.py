# 입력
n, m = map(int, input().split()) # n:강의 수, m:블루레이 수
course_time_list = list(map(int, input().split())) #각 강의의 길이

#구해야 하는 것: 최소 녹화 길이
start, end = max(course_time_list), sum(course_time_list)
while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 1
    for course in course_time_list:
        if total + course > mid:
            cnt += 1
            total = 0
        total += course
    if cnt <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)


