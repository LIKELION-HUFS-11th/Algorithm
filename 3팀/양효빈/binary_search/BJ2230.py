### 수 고르기

# 두 수의 차이가 m 이상이면서 가장 작게
# 차이 출력
# m 이상일 때 차이를 더 작게
# m 미만일 때 차이를 더 크게
# 즉 차이를 좁힐 뿐만 아니라 넓히는 경우도 생각 -> two pointer 방법


n, m = map(int, input().split())
number_list = [int(input()) for _ in range(n)]
number_list.sort()


def two_pointer(left, right):
    ans = float('inf')

    while left < n and right < n:
        diff = number_list[right] - number_list[left]
        # m보다 차이가 작으면 차이 넓혀주기
        if diff < m:
            right += 1
        # 차이가 m보다 크거나 같으면 ans값 바꿔주고 차이 좁히기
        elif diff > m:
            ans = min(diff, ans)
            left += 1
        # m과 차이가 동일하면 바로 리턴
        else:
            return diff
    return ans


# left, right 모두 0부터 시작하여 오른쪽 한 방향으로만 이동
print(two_pointer(0, 0))


# m은 항상 0 이상이므로 left와 right의 값이 동일해지면 바로 차이를 넓혀주기 때문에
# left가 right를 넘을 경우에 대한 조건을 따로 설정하지 않아도 된다