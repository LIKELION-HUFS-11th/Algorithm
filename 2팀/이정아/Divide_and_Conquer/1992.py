import sys
input = sys.stdin.readline

n = int(input())
pows = [1, 2, 4, 8, 16, 32, 64]
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

def dc(x, y, i):
    if i == 0:
        return f"{arr[x][y]}"
    basis = arr[x][y]
    for a in range(2**i):
        for b in range(2**i):
            if basis != arr[x+a][y+b]:
                i -= 1
                s1 = dc(x, y, i)
                s2 = dc(x, y+2**i, i)
                s3 = dc(x+2**i, y, i)
                s4 = dc(x+2**i, y+2**i, i)
                return f"({s1}{s2}{s3}{s4})"
    return basis

maxpow = pows.index(n)
if maxpow == 0:
    print(arr[0][0])
else:
    print(dc(0, 0, maxpow))
