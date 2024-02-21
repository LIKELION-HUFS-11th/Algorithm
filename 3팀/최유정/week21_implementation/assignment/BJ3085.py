from copy import deepcopy

N = int(input())

def check_row(board, s, e):
    max_cnt = 0
    for i in range(s, e+1):
        cnt = 1
        start = board[0][i]
        for j in range(1, N):
            if board[j][i] == start:
                cnt += 1
            else:
                start = board[j][i]
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

def check_column(board, s, e):
    max_cnt = 0
    for i in range(s, e+1):
        cnt = 1
        start = board[i][0]
        for j in range(1, N):
            if board[i][j] == start:
                cnt += 1
            else:
                start = board[i][j]
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt


board = [list(input()) for _ in range(N)]
max_result = max(check_column(board, 0, N-1), check_row(board, 0, N-1))

for i in range(N):
    for j in range(N):
        if j < N-1 and i < N-1:
            if board[i][j] != board[i][j+1]:
                copy_board1 = deepcopy(board)
                copy_board1[i][j] = board[i][j+1]
                copy_board1[i][j+1] = board[i][j]
                max_result = max(max_result, check_row(copy_board1, j, j+1), check_column(copy_board1, i, i))
            if board[i][j] != board[i+1][j]:
                copy_board2 = deepcopy(board)
                copy_board2[i][j] = board[i+1][j]
                copy_board2[i+1][j] = board[i][j]
                max_result = max(max_result, check_column(copy_board2, i, i+1), check_row(copy_board2, j, j))
        elif j < N-1 and board[i][j+1] != board[i][j]:
            copy_board1 = deepcopy(board)
            copy_board1[i][j] = board[i][j+1]
            copy_board1[i][j+1] = board[i][j]
            max_result = max(max_result, check_row(copy_board1, j, j+1), check_column(copy_board1, i, i))
        elif i < N-1 and board[i+1][j] != board[i][j]:
            copy_board2 = deepcopy(board)
            copy_board2[i][j] = board[i+1][j]
            copy_board2[i+1][j] = board[i][j]
            max_result = max(max_result, check_column(copy_board2, i, i+1), check_row(copy_board2, j, j))
print(max_result)