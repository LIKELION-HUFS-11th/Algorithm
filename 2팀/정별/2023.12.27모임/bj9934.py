#중위 순회 결과를 주었을 때, 처음 트리를 복원하라


k = 2
result = [2, 1, 3]


# mid = len(result) //2 + 1
# ans.append(mid)


def unorder(res):
    ans = []
    if res:
        mid = len(res) //2 + 1
    
    ans.append(mid)
    
    unorder(res[:mid])
    unorder(res[mid+1:])


        

