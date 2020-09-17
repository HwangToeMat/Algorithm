from itertools import combinations
import collections


def solution(orders, course):
    answer = []
    tmp = {}
    tmp_course = {}
    orders = list(map(list, orders))
    orders = list(map(lambda x: sorted(x), orders))
    for _ in range(len(orders)):
        tmp[_+1] = []
    for _ in course:
        tmp_course[_] = []
    # 1. course 사이즈에 맞는 조합 전부 구하기
    for i in range(len(orders)):
        for _ in course:
            if len(orders[i]) < _:
                continue
            tmp_comb = list(combinations(orders[i], _))
            tmp[i + 1].extend(tmp_comb)
            tmp_course[_].extend(tmp_comb)
    # 2. collection으로 빈도 구하기
    ans = []
    for _ in course:
        lst_cnt = dict(collections.Counter(tmp_course[_]))
        for (k, v) in lst_cnt.items():
            if v == max(list(lst_cnt.values())) and v > 1:
                ans.append(k)
    answer = sorted(list(map(lambda x: ''.join(x), ans)))

    return answer
