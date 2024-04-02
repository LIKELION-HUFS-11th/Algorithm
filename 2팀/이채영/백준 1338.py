import sys
input = sys.stdin.readline

def choose_position(height, goal):
    global line

    cnt = 0
    i = 0
    # for i in range(len(line)):
    while True:
        if cnt == goal:
            line.insert(i, height)
            break
        
        if line[i] > height:
            cnt += 1

        i += 1

    return




n = int(input().strip())

people = list(map(int, input().split()))
people.reverse() #[0, 1, 2, 3, 4, 5] 키[6, 5 ,4, 3, 2,1]
# line = []

# print(people)

for i in range(0, n):
    if i == 0:
        continue
    
    elif i == 1: #2번째로 키큰 사람
        if people[i] == 1: #제일 키큰 사람(i-1)이 자기보다 왼쪽에 있음
            line = [n, n-i]
        else:
            line = [n-i, n]

    
    else:
        height = n - i
        choose_position(height, people[i])


for elem in line:
    print(elem, end=" ")