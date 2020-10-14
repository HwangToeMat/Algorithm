def solution(n):
    return convert(n, 3)


def convert(n, base):
    T = '124'
    q, r = divmod(n-1, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
