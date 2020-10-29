from itertools import combinations


def solution(relations):
    answer = 0
    dataframe = {}
    for r in relations:
        for i, d in enumerate(r):
            if dataframe.get(i) == None:
                dataframe[i] = [d]
            else:
                dataframe[i].append(d)
    cnt = 1
    ans_lst = []
    while dataframe != {}:
        if cnt > len(dataframe.keys()):
            break
        tmp = {}
        value = list(dataframe.values())
        for idx in range(len(value[0])):
            relation = [_[idx] for _ in value]
            key = list(dataframe.keys())
            key_lst = list(combinations(key, cnt))
            lst = list(combinations(relation, cnt))
            for idx, l in enumerate(lst):
                i = key_lst[idx]
                if tmp.get(i) == None:
                    tmp[i] = [l]
                else:
                    tmp[i].append(l)

        for k, v in tmp.items():
            if len(v) == len(set(v)):
                ck = True
                kk = set(k)
                for a in ans_lst:
                    if a.issubset(kk):
                        ck = False
                        break
                if ck:
                    answer += 1
                    ans_lst.append(kk)

        cnt += 1
    return answer
