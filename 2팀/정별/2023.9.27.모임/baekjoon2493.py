#이렇게 말고 스택으로 풀기.
#시간제한에 걸린다.

# n = int(input())
# arr = list(map(int, input().split()))
# ans = [0]*n


# # for i, top in enumerate(arr):
    

    
# for j in range(len(arr)-1,0, -1): #메인.
#     for l in range(len(arr)-2,0, -1): #비교
#         if arr[l] >= arr[j] and l <j :
#             ans[j] = l+1
#             break

# for elem in ans:
#     print(elem, end=' ')



def towers(n, heights):
    arr = [0] * n 
    stack = []  
    
    for i in range(n):
        # 스택이 비어있지 않고, 동시에 현재 탑의 높이가 스택의 맨 위 탑보다 크거나 같을 때
        # 왼쪽을 향해 지금 탐색중인 탑의 높이보다 낮으면 스택값을 그냥 빼버림
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()  # 스택에서 이전 탑 제거
        if stack:
            arr[i] = stack[-1] + 1  # 현재 탑의 결과를 스택의 맨 위 탑으로 설정
        stack.append(i)  # 현재 탑의 인덱스 값을 스택에 추가
    
    return arr

# 입력 받기
n = int(input())
heights = list(map(int, input().split()))
answer = towers(n, heights)

print(" ".join(map(str, answer)))