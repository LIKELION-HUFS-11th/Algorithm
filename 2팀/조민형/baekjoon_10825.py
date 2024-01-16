studentNum = int(input(""))

result = []
for i in range(studentNum):
    studentNameAndScore = input().split()
    result.append(studentNameAndScore)

result.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in result:
    print(student[0])
    



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

