import collections


def solution(genres, plays):
    A = {}
    A_sum = {}
    answer = []
    for _, (k, v) in enumerate(zip(genres, plays)):
        if k in A.keys():
            A[k][_] = v
            A_sum[k] += v
        else:
            A[k] = {_: v}
            A_sum[k] = v
    A_sum = dict(sorted(A_sum.items(), key=lambda x: x[1], reverse=True))
    for i in A_sum.keys():
        tmp = sorted(A[i].items(), key=lambda x: x[1], reverse=True)
        answer.append(tmp[0][0])
        if len(tmp) > 1:
            answer.append(tmp[1][0])

    return answer
