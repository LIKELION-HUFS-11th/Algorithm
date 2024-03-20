# n = int(input())
# nData = [input().split() for _ in range(n)]
# for i in range(n):
#     nData[i][1] = int(nData[i][1])
#     nData[i][2] = int(nData[i][2])
#     nData[i][3] = int(nData[i][3])

# print(nData)

# nData.sort(key=lambda x : (-x[i][1], x[i][2], -x[3], x[0]))

# print(nData[0])

studentNum = int(input(""))

result = []
for i in range(studentNum):
    studentNameAndScore = input().split()
    result.append(studentNameAndScore)
print

result.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in result:
    print(student[0])





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





# #민형이가 푼 방식. runtime error 떴지만 답은 잘 떴음
# studentNum = int(input(""))

# result = []

# for i in range(studentNum):
#     studentNameAndScore = input("")
#     studentNameAndScore = studentNameAndScore.split(" ")
#     if not result:
#         result.append(studentNameAndScore)
#     else:
#         j = 0
#         while j < len(result):
#             if int(studentNameAndScore[1]) > int(result[j][1]):   
#                 result.insert(j, studentNameAndScore)
#                 break
#             elif int(studentNameAndScore[1]) == int(result[j][1]):
#                 k = j
#                 while k < len(result):
#                     if int(studentNameAndScore[2]) > int(result[k][2]) and int(studentNameAndScore[1]) == int(result[k][1]):
#                         k+=1
#                         continue
#                     elif int(studentNameAndScore[2]) > int(result[k-1][2]) and int(studentNameAndScore[1]) == int(result[k-1][1]):
#                         result.insert(k, studentNameAndScore)
#                         break
#                     elif int(studentNameAndScore[2]) == int(result[k][2]):
#                         l = k
#                         while l < len(result):
#                             if int(studentNameAndScore[3]) > int(result[l][3]) and int(studentNameAndScore[2]) == int(result[l][2]):
#                                 result.insert(l, studentNameAndScore)
#                                 break
#                             elif int(studentNameAndScore[3]) == int(result[l][3]):
#                                 a = l
#                                 while a < len(result):
#                                     if studentNameAndScore[0] < result[a][0] and int(studentNameAndScore[3]) == int(result[k][3]):
#                                         result.insert(a, studentNameAndScore)
#                                         break
#                                     elif a == len(result)-1:
#                                         result.append(studentNameAndScore)
#                                         break                             
#                                     a += 1
#                                 break
#                             elif l == len(result)-1:
#                                 result.append(studentNameAndScore)
#                                 break                             
#                             l+=1
#                         break
#                     elif k == len(result)-1:
#                         result.append(studentNameAndScore)
#                         break
#                     k+=1
#                 break
#             elif j == len(result)-1 :
#                 result.append(studentNameAndScore)
#                 break
#             j+=1


# for b in range(len(result)):
#     print(result[b][0])