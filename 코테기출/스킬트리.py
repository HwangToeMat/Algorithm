def solution(skill, skill_trees):
    answer = len(skill_trees)
    sk_lst = list(skill)
    tr_lst = list(map(lambda x: list(x), skill_trees))
    for tr in tr_lst:
        tmp = 1
        for idx, i in enumerate(tr):
            if tmp == len(sk_lst):
                break
            if i in sk_lst[tmp:]:
                answer -= 1
                break
            elif i == sk_lst[tmp-1]:
                tmp += 1
    return answer
