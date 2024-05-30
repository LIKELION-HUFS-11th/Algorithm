n = int(input())
numbers = list(map(int, input().split()))
answer = sorted(numbers, reverse=True)
maxcnt = int(input())
idx = 0
cnt = 0
while cnt < maxcnt:
    if numbers == answer:
        break
    if idx == n-1:
        idx = 0
    if numbers[idx+1] > numbers[idx]:
        numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
        cnt += 1
    idx += 1
for number in numbers:
    print(number, end=" ")
print()