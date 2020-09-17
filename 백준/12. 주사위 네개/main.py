N = int(input())


def cal():
    A = sorted(list(map(int, input().split())))
    if len(set(A)) == 1:
        tmp = A[0]
        return 50000 + 5000 * tmp
    elif len(set(A)) == 2:
        if A[0] != A[1]:
            return 10000 + 1000 * A[1]
        else:
            return 2000 + 500 * A[1] + 500 * A[2]
    elif len(set(A)) == 3:
        if A[0] == A[1]:
            tmp = A[0]
        elif A[1] == A[2]:
            tmp = A[1]
        else:
            tmp = A[2]
        return 1000 + 100 * tmp
    else:
        return 100 * A[3]


score = []

for _ in range(N):
    score.append(cal())

print(max(score))
