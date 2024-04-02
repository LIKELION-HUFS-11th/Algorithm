import sys

n = int(sys.stdin.readline())

printList = []
def hanoi(n, start, mid, to):
    global printList
    if n == 1 :
        printList.append(f"{start} {to}")
        return
    hanoi(n-1, start,to,mid)
    printList.append(f"{start} {to}")
    hanoi(n-1,mid,start,to)
hanoi(n,1,2,3)
print(2**n-1)
for i in printList: print(i)

    