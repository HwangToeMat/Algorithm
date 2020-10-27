def solution(m, n, board):
    while True:
        tmp = chk(m, n, board)
        if tmp == board:
            break
        else:
            board = down(m, n, tmp)
    return sum(map(lambda x: x.count(1), board))


def new_arr(m, n, k):
    return [[k for i in range(n)] for j in range(m)]


def down(m, n, board):
    ck = new_arr(m, n, 1)
    for i in range(n):
        cnt = m - 1
        for j in range(m-1, -1, -1):
            if board[j][i] != 1:
                ck[cnt][i] = board[j][i]
                cnt -= 1
    return ck


def chk(m, n, board):
    ck = new_arr(m, n, 0)
    for i in range(n):
        for j in range(m):
            if j + 1 < m and i + 1 < n and board[j][i] == board[j + 1][i] and board[j+1][i] == board[j + 1][i+1] and board[j + 1][i+1] == board[j][i+1]:
                ck[j][i] = 1
                ck[j+1][i] = 1
                ck[j][i+1] = 1
                ck[j+1][i+1] = 1
            else:
                if ck[j][i]:
                    continue
                ck[j][i] = board[j][i]
    return ck
