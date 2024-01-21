n = int(input())
nData = [input().split() for _ in range(n)]
for i in range(n):
    nData[i][1] = int(nData[i][1])
    nData[i][2] = int(nData[i][2])
    nData[i][3] = int(nData[i][3])
    nData[i].append(i) #고유번호임.

print(nData)

nData.sort(key=lambda x : (-x[i][1], x[i][2], -x[i][3], x[i][0]))

print(nData[0])



# # nData[1]
# # [2] [3]
# # [4] 각각 분할 정복

nKor = [[nData[i][1], nData[i][0]] for i in range(n)]
nEng = [nData[i][2] for i in range(n)]
nMat = [nData[i][3] for i in range(n)]
sNam = [nData[i][0] for i in range(n)]



def merge(a, b):
    result = []
    i = j = 0
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    result.extend(a[i:])
    result.extend(b[j:])
    
    return result

def sort_students(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums

    a = sort_students(nums[:len(nums) //2])
    b = sort_students(nums[len(nums) //2:])
    
    return merge(a,b)

def move_backword(num, n):
    for _ in range(n):
        n0, n1, n2, n3 = num[0], num[1], num[2], num[3]
        

x = sort_students(nKor)
sorted_Kor = x[::-1]
# print(x)
# x = sort_students([50, 80, 80, 50, 50, 60, 80, 70, 70, 70, 80, 50])
# print(x[::-1])

    