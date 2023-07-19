import sys  # input보다 좀 더 빠른 입력을 위해

line = sys.stdin.readline()
line = line.upper()
pelin = ""  # 뒤집힌 문자열을 담을 변수

for i in line:

    if 64 > ord(i) or ord(i) > 90:  # 아스키코드 변환시 영 대문자가 아니면
        line = line.replace("%s" % i, "")  # 날려버림

pelin = line[::-1]  # 슬라이싱 활용해서 거꾸로 담았음

if line == pelin:
    print("True")

else:
    print("False")
