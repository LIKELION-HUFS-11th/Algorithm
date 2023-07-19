# 입력
s = input()

# 설계
# s_list
s_list = list(s)

# num_list, str_list
num_list, str_list = [], []

for s in s_list:
    try:
        num_list.append(int(s))
    except:
        str_list.append(s)

str_list.sort()
sum_num = sum(num_list)

for s in str_list:
    print(s, end='')
print(sum_num)
