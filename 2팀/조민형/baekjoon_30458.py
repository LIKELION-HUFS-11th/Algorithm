import sys
from collections import Counter

N = int(sys.stdin.readline())
full_string = sys.stdin.readline().rstrip('\n')

if N % 2 != 0:
    string_left = full_string[:(N//2)]
    string_right = full_string[(N//2)+1 :]
else: 
    string_left = full_string[:(N//2)]
    string_right = full_string[(N//2) :]
    
left_counted = Counter(string_left)
right_counted = Counter(string_right)

full_counted = left_counted + right_counted

for i in full_counted.values():
    if i % 2 != 0:
        print("No")
        sys.exit()
print("Yes")