from copy import deepcopy


def solution(key, lock):
    answer = False
    tmp_l = pad(lock, len(key))
    for _ in range(4):
        key = rotate(key, len(key))
        for i in range(len(key)+len(lock) - 1):
            for j in range(len(key)+len(lock) - 1):
                X = deepcopy(tmp_l)
                for ii in range(len(key)):
                    for jj in range(len(key)):
                        if tmp_l[i+ii][j+jj] == -1:
                            continue
                        else:
                            X[i+ii][j+jj] = tmp_l[i+ii][j+jj] + key[ii][jj]
                if sum(map(lambda x: x.count(0) + x.count(2), X)) == 0:
                    for _ in X:
                        print(_)
                    answer = True
                    return answer
    return answer


def pad(arr, n):
    ck = [[-1 for j in range(len(arr) + n*2 - 2)]
          for i in range(len(arr) + n*2 - 2)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            ck[n-1+i][n-1+j] = arr[i][j]
    return ck


def rotate(arr, n):
    X = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            X[n-j-1][i] = arr[i][j]
    return X
