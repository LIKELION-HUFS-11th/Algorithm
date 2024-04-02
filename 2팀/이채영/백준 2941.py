# https://www.acmicpc.net/problem/2941

# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

# cro_two_words = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
# cro_three_words = ["dz="]

str = input()

i = 0
cnt = 0
while i < len(str):
    if i + 2 < len(str) and str[i] == "d" and str[i+1] == "z" and str[i+2] == "=":
        i += 3
    elif i + 1 < len(str) and str[i+1] in "=-" and str[i] in "cdsz":
        i += 2
    elif i + 1 < len(str) and str[i+1] == 'j' and str[i] in "ln":
        i += 2
    else:
        i += 1
    
    cnt += 1

print(cnt)