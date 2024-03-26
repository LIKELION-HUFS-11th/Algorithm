import sys
T = int(sys.stdin.readline())

def search(num, start, end):
    if start > end:
        return False
    mid = (start + end) //2
    if note1[mid] == num:
        return True
    elif note1[mid] > num:
        end = mid - 1
    elif note1[mid] < num:
        start = mid + 1
    return search(num, start, end)
    

for _ in range(T):
    n = int(sys.stdin.readline())
    note1= list(map(int,sys.stdin.readline().split()))
    note1.sort()
    m = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))
    result = []
    for i in note2:
        if search(i, 0, len(note1)-1) == True:
            result.append(1)
        else:
            result.append(0)
    for j in result: print(j)
    
