def solution(n, arr1, arr2):
    a1 = list(map(lambda x: format(x, 'b').zfill(n), arr1))
    a2 = list(map(lambda x: format(x, 'b').zfill(n), arr2))
    answer = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if a1[i][j] == '1' or a2[i][j] == '1':
                tmp += '#'
            elif a1[i][j] == '0' and a2[i][j] == '0':
                tmp += ' '
        answer.append(tmp)
    return answer
