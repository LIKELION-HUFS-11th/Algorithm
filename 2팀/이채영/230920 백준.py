# N = int(input())

# t = list(map(int, input().split()))
# towers = [0]
# for elem in t:
#     towers.append(elem)

# contact = [0 for _ in range(N+1)] #0번째 인덱스는 사용하지 않음

# max_height = towers.index(max(towers))

# for i in range(1, N+1):
#     if i-1 < 1 or i == max_height:
#         contact[i] = 0
#         continue
    
#     else:
#         #Sol1
#         # for j in range(i-1, 0, -1):
#         #     if j < 1:
#         #         contact[i] = 0
#         #         break
#         #     else:
#         #         if towers[j] >= towers[i]:
#         #             contact[i] = j
#         #             break

#         #Sol2
#         # [6, 9, 5, 7, 4]
#         if i < max_height:
#             for j in range(i-1, 0, -1):
#                 if j < 1:
#                     contact[i] = 0
#                     break
#                 else:
#                     if towers[j] >= towers[i]:
#                         contact[i] = j
#                         break
#         else:
#             for j in range(i+1, N+1):
#                 if towers[j] >= towers[i]:
#                     contact[i] = j
#                     break


# for i in range(1, N+1):
#     print(contact[i], end=" ")

#스택으로 풀어보기 


class Stack:
    def __init__(self):
        self.top = [0]

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        return self.top[-1]


N = int(input())
S = Stack()

t = list(map(int, input().split()))
towers = [0]
for elem in t:
    towers.append(elem)

contacted = [0 for _ in range(N+1)]

p = N
for i in range(N, 0, -1):
    if i < 1:
        continue

    if S.pop() < towers[i]:
        S.push(towers[i])

        while p != i:
            contacted[p] = i
            p -= 1


for i in range(N+1):
    if i != 0:
        print(contacted[i], end=" ")