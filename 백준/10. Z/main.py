N, r, c = map(int, input().split())


def Z(N, r, c):
    if N == 0:
        return 0
    tmp = 2**(N-1)
    if tmp >= r and tmp >= c:
        ret = 0
    elif tmp >= r and tmp < c:
        ret = tmp**2
        c -= tmp
    elif tmp < r and tmp >= c:
        ret = 2 * (tmp**2)
        r -= tmp
    else:
        ret = 3 * (tmp**2)
        r -= tmp
        c -= tmp
    return ret + Z(N-1, r, c)


print(Z(N, r+1, c+1))
