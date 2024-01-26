#교재 풀이

a = 1
b = 7

MASK = 0xFFFFFFFF
INT_MAX = 0x7FFFFFFF #양의 정수 최댓값. 32비트에서

while b != 0:
    a,b = (a ^ b) & MASK, ((a & b) << 1) & MASK #sum, carry 처리

if a >INT_MAX:  #a 맨 앞 자리수가 음수면 1이 붙음. INT_MAX는 양수라 맨 앞 0.
    a = ~(a ^ MASK)


print(a)

#변형
a = 5
b = -3

MASK = 0xFFFFFFFF
INT_MAX = 0x7FFFFFFF

while b != 0:
    temp_a = a
    a = (a ^ b) & MASK  # 전가산기에서 sum 처리
    b = ((temp_a & b) << 1) & MASK  # carry 처리

if a & (1 << 31):  #1을 왼쪽으로 31번 이동 = 2의 31제곱
    a = ~(a ^ MASK)

print(a)
