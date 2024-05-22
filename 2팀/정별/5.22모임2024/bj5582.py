#참고 사이트: https://velog.io/@crash1522/%EB%B0%B1%EC%A4%80-5582-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4

def str_(i):
    cnt = 0
    rtn = 0
    if i < 0:
        j = -i
        i = 0
    else:
        j = 0
    while j  < len(str2):
        if str1[i] == str2[j]:
            cnt += 1
            rtn = max(rtn, cnt)
        else:
            cnt = 0
        i += 1
        j += 1
        if i >= len(str1):
            return rtn
    return rtn

str1 = list(input())
str2 = list(input())
if len(str2) > len(str1):
    tem = str1
    str1 = str2
    str2 = tem
ans = 0
for i in range(-1 * len(str2) + 1, len(str1)):
    ans = max(ans, str_(i))
print(ans)