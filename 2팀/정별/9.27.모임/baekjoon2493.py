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
    
    for i in range(N):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()  
        if stack:
            arr[i] = stack[-1] + 1

        stack.append(i)  
    
    return arr

N = int(input())
heights = list(map(int, input().split()))

answer = towers(N, heights)

print(" ".join(map(str, answer)))
