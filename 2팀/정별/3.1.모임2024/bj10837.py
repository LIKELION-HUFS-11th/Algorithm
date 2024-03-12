#28점
#128ms
import sys

def main():
    K = int(input().strip())
    C = int(input().strip())

    for c in range(C):
        M, N = map(int, input().strip().split())

        # 영희 동수 동점.
        if M - N == 0:
            print(1)
            continue

        remain_games = K - max(M, N)
        diff = abs(M - N)

        # 영희가 더 큼
        if M > N:
            if diff - remain_games <= 2:
                print(1)
                continue
            print(0)
            continue

        # 동수가 더 큼
        if diff - remain_games <= 1:
            print(1)
            continue

        print(0)

if __name__ == "__main__":
    main()
