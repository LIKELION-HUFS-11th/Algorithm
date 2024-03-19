# import sys
# input = sys.stdin.readline

# text = list(input())
# n = len(text)
# text.remove(text[n -1])
# cursor = n - 1

# m = int(input())
# for i in range(m):
#     rule = input()
#     if rule[0] == 'L' and cursor != 0:
#         cursor -= 1
#     elif rule[0] == 'D' and cursor != (n - 1):
#         cursor += 1
#     elif rule[0] == 'B' and cursor != 0:
#         text.remove(text[cursor])
#         cursor -= 1
#     elif rule[0] == 'P':
#         text.insert(cursor, rule[2])
#         cursor += 1
# print(''.join(text))

import sys
input = sys.stdin.readline

left_stack = []
right_stack = []

text = input().strip()
for char in text:
    left_stack.append(char)

m = int(input())
for _ in range(m):
    rule = input().split()
    if rule[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif rule[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif rule[0] == 'B' and left_stack:
        left_stack.pop()
    elif rule[0] == 'P':
        left_stack.append(rule[1])

print(''.join(left_stack + right_stack[::-1]))
