def solution(triangle):
    answer = 0
    tmp = [[0, 0]]
    for t in triangle:
        a = [0]
        b = [0]
        a.extend(t)
        a.extend(b)
        tmp.append(a)
    for i in range(1, len(triangle) + 1):
        for j in range(1, len(tmp[i]) - 1):
            k = max(tmp[i][j] + tmp[i-1][j], tmp[i][j] + tmp[i-1][j-1])
            tmp[i][j] = k
    answer = max(tmp[-1])

    return answer
