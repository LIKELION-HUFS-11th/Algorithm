### 두 용액
# 합이 가장 0에 가깝게 하는 두 숫자 출력



### solution 1 ###
# 답은 제대로 나오나 시간 초과 오답
# 이진탐색 방식

## idea ##
# mid = 양수, left = 음수 -> mid와 (mid+1)합 / mid와 left 합 -> 왼쪽 계속 탐색
# mid = 양수, left = 양수 -> left와 (left+1)합 반환
# mid = 음수, right = 양수 -> mid와 mid-1합 / mid와 right 합 -> 오른쪽 계속 탐색
# mid = 음수, right = 음수 -> right와 right-1 합 반환
# 합의 절댓값이 가장 작은 수 반환



# 용액 수
n = int(input())
# 오름차순 정렬한 용액 리스트
solution = list(map(int, input().split()))
solution.sort()
# 정답 리스트
answer = [solution[0], solution[n-1]]


# 대소비교
def comparison(left, right, answer):
    if abs(left + right) < abs(sum(answer)):
        answer = [left, right]

# 이진탐색
def binary_search(arr, left, right, answer):
    mid = (left+right) // 2
    while left <= right:
        if mid > 0:
            if left < 0:
                comparison(arr[mid], arr[mid+1], answer)
                comparison(arr(left), arr[mid], answer)
                binary_search(arr, left, mid)
            else:
                comparison(arr[left], arr[left+1], answer)
        else:
            if right < 0:
                comparison(arr[mid], arr[mid-1], answer)
                comparison(arr(mid), arr[right], answer)
                binary_search(arr, mid, right)
            else:
                comparison(arr[right-1], arr[right], answer)

# 출력
binary_search(solution, 0, n-1, answer)
print(answer[0], answer[1])






### solution 2 ###
# 시간 초과 문제 해결 - O(NlogN) 정답
# 두 포인터(two pointer) 방식


n = int(input())
solution = list(map(int, input().split()))
solution.sort() # 리스트 정렬 O(NlogN)

# 초기 정답 설정
ans = [solution[0], solution[n-1]]
min_sum = abs(sum(ans))

left = 0
right = n - 1

# 두 개의 포인터를 활용하여 용액 리스트 순회 O(N)
while left < right:
    current_sum = solution[left] + solution[right]

    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        ans = [solution[left], solution[right]]

    # 0에 더 가까워져야 하므로 음수 방향에서 양수 방향으로
    if current_sum < 0:
        left += 1
    # 양수 방향에서 음수 방향으로
    else:
        right -= 1

print(ans[0], ans[1])





### solution 3 ###
# 이진탐색
# 틀림

n = int(input())
solution = list(map(int, input().split()))
solution.sort()


def near_zero(arr, n):
    left, right = 0, n-1
    ans_list = [arr[0], arr[1]]
    ans = abs(sum(ans_list))

    while left <= right:
        mid = (left + right) // 2
        tmp = arr[left] + arr[right]

        if abs(tmp) <= ans:
            ans = abs(tmp)
            ans_list = [arr[left], arr[right]]
            if tmp < 0:
                left = mid + 1
            else:
                right = mid - 1
        else:
            ans = abs(tmp)
            ans_list = [arr[left], arr[right]]
            if tmp < 0:
                left = mid + 1
            else:
                right = mid - 1

    return ans_list


ans = near_zero(solution, n)
print(ans[0], ans[1])
