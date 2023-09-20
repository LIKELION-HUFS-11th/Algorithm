str = input()

str_list = [0 for _ in range(26)]

for x in str:
    i = ord(x) - 97 # 문자 -> 아스키코드로 변환 아스키코드 97 = 소문자 'a'
    if str_list[i] == 0:
        str_list[i] += 1
    else:
        continue

for i in range(len(str_list)):
    if str_list[i] != 0:
        print(chr(i+97), end="") #아스키코드 -> 문자로 변환