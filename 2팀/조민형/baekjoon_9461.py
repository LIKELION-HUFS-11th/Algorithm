import sys

T = int(sys.stdin.readline())

sequence_list = [1,1,1]
def sequence(n):
    if n < len(sequence_list):
        return sequence_list[n-1]
    else:
        for _ in range(len(sequence_list),n):
            sequence_list.append(sequence_list[-2] + sequence_list[-3])
        return sequence_list[n-1]
    

for _ in range(T):
    N = int(sys.stdin.readline())
    print(sequence(N))