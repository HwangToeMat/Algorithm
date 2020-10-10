def solution(n):
    answer = []
    lst = [[0 for __ in range(_)] for _ in range(1, n+1)]
    cnt, ck = 0, 0
    A = [0, -1]
    while n:
        if ck % 3 == 0:
            for _ in range(1, n+1):
                cnt += 1
                A[1] += 1
                lst[A[1]][A[0]] = cnt
        elif ck % 3 == 1:
            for _ in range(1, n+1):
                cnt += 1
                A[0] += 1
                lst[A[1]][A[0]] = cnt
        else:
            for _ in range(1, n+1):
                cnt += 1
                A[1] -= 1
                A[0] -= 1
                lst[A[1]][A[0]] = cnt
        ck += 1
        n -= 1
    for i in lst:
        for j in i:
            answer.append(j)
    return answer
