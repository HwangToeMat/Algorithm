from copy import deepcopy


def solution(name):
    alp = {chr(_): min(_-65, 26-(_-65)) for _ in range(65, 91)}
    answer = 0
    idx = 0
    dis = 0
    fin = False
    test = deepcopy(name)
    test.rstrip('A')
    for _ in range(len(name)):
        if name[_] == 'A':
            continue
        if not fin:
            if len(test)-1 > idx*2+len(name)-_:
                fin = True
                dis = min(idx*2 + len(name)-_, (len(name)-_)*2 + idx)
            else:
                dis += _ - idx
                idx = _
        answer += alp[name[_]]
    answer += dis
    return answer
