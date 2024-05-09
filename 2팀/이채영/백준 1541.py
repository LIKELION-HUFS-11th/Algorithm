"""
240508 스터디
풀이중..
"""

# import sys
# input = sys.stdin.readline

# def calculate(x, y, op):
#     if op == '-':
#         return x - y
#     elif op == '+':
#         return x + y

# e = input()
# e_list = [] #['10', '+', '20', '+', '30', '+', '40']
# op_list = []

# all_plus = True
# s = ""
# for i in range(len(e)):
#     if i == len(e)-1:
#         e_list.append(int(s))
#     if s == "0":
#         s = ""

#     if e[i] in '-+':
#         if e[i] == '-':
#             all_plus = False
#         e_list.append(int(s))
#         s = ""

#         e_list.append(e[i])
#         op_list.append(e[i])
#     else:
#         s += e[i]

# # print(e_list)

# # 괄호는 - 앞
# # 최대한 많이 빼야함 

# if len(op_list) <= 1:
#     res = calculate(e_list[0], e_list[2], e_list[1])

# elif all_plus == True:
#     res = 0
#     for i in range(0, len(e_list) - 1, 2):
#         res += e_list[i]

# else:
#     total = 0
#     for op in range(1, len(e_list)-2, 2):
#         if op == '-':
#             sub = 0
#             max_sub = -sys.maxsize
#             max_sub_index = op #괄호를 닫는 인덱스

#             for j in range(op+2, len(e_list)-2, 2):
#                 sub += calculate(e_list[j-1], e_list[j+1], e_list[j])
#                 if sub > max_sub:
#                     max_sub = sub
#                     max_sub_index = j
#         elif op == '+':
            
