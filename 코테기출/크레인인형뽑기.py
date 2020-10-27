def solution(board, moves):
    answer = 0
    container = [None]
    for m in moves:
        idx = m-1
        for _, b in enumerate(board):
            if b[idx] == 0:
                continue
            else: 
                if container[-1] == b[idx]:
                    container.pop()
                    board[_][idx] = 0
                    answer += 2
                else:
                    container.append(b[idx])  
                    board[_][idx] = 0
                break
    return answer