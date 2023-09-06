### 나무 자르기
# 목재 절단기 높이 H의 최댓값 구하기

# 목재 절단기 높이 = H 
# H - 나무 양수일 때 합과 7 비교
# 7보다 클 때 right + 1
# 7보다 작을 때 left + 1
# right와 left 교차 시 H 반환



# 입력
n, m = map(int, input().split())
# 나무 리스트 + 오름차순 정렬
tree = list(map(int, input().split()))
tree.sort()


def cutter(tree_arr, needed_tree):
    left, right = 0, max(tree_arr)

    while left <= right:
        # 절단기 높이
        mid = (left + right) // 2
        total = 0
        # 자른 나무의 높이 합
        for tree in tree_arr:
            if (tree - mid) > 0:
                total += (tree - mid)
        
        # 절단기 높이를 높여야 하는 경우
        if total >= needed_tree:
            left = mid + 1
        # 절단기 높이를 낮춰야 하는 경우
        else:
            right = mid - 1

    return right


ans = cutter(tree, m)
print(ans)