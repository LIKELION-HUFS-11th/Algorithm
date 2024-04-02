#중위 순회 결과를 주었을 때, 처음 트리를 복원하라
#처음 트리는 레벨 순회 형태로 추출

k = int(input())
result = list(map(int, input().split()))
answer = []

for _ in range(k): #층별로 리스트 비워두기
    answer.append([])

# answer=[
#     [ 3],  0층
#     [6 2],  1층
#     [ 1 4 5 7],  2층
#     [ ], ,,,,
# ]

def unorder(res, i): #i는 return할 최종 트리에서, 각 층의 인덱스값
    mid =len(res)//2 #각 서브트리들의 루트 노드 인덱스 값
    answer[i].append(res[mid]) #루트노드는 기본적으로 추가
    
    if len(res) == 1:
        return #리프노드에선 자식 없으니까, 본인 노드 하나만 추가
    
    unorder(res[:mid], i+1) 
    unorder(res[mid+1:], i+1)
    
unorder(result, 0) #입력값으로 트리 만들어두기
for i in range(k):
    print(*answer[i])



# def unorder(res):
#     global layer
#     global i
#     if res:
#         mid_idx = len(res) // 2  #인덱스 값임

#         ans.append(res[mid_idx])
#         layer+=1
        
#         left_idx = len(res[:mid_idx]) // 2
#         ans.append(res[left_idx])
        
#         right_idx = mid_idx + len(res[mid_idx+1:])//2
#         ans.append(res[right_idx])
                
#         # ans.append(res[mid]) #루트 값 추가하기


#         print(layer)
        
#         unorder(res[:mid_idx]) #왼쪽 서브트리의 루트 값 추가
#         unorder(res[mid_idx+1:]) #오른쪽 서브트리의 루트 값 추가
    
#     return ans
 



        

