from itertools import combinations


def solution(clothes):
    C = {}
    ans = 1
    for v, k in clothes:
        if k in C.keys():
            C[k] += 1
        else:
            C[k] = 1

    for _ in C.values():
        ans *= _+1
    return ans - 1
