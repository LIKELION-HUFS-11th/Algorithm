
N = int(input())

S = list(input())


unmatched_list = []
# unmatched_left = []
# unmatched_right = [] #set 안됨! 중복 허용 안되니까

if N % 2 == 1:
    i, j = N // 2 - 1, N // 2 + 1
else:
    i, j = N // 2, N // 2 + 1

while i >= 0 and j <= N - 1:
    if S[i] != S[j]:
        unmatched_pair = {S[i], S[j]}
        if unmatched_pair in unmatched_list:
            unmatched_list.remove(unmatched_pair)
        else:
            unmatched_list.append({S[i], S[j]})

        # unmatched_left.append(S[i])
        # unmatched_right.append(S[j])

    i -= 1
    j += 1


if not unmatched_list:
    print("Yes")
else:
    print("No")
    
# unmatched_left.sort()
# unmatched_right.sort()
    
# if unmatched_left == unmatched_right:
#     print("Yes")
# else:
#     print("No")