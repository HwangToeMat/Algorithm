def solution(p):
    answer = ''
    if p == '':
        return ''
    lst = chg(p)
    answer = sep(lst)

    return answer


def sep(lst):
    if lst == []:
        return ''
    elif lst == [1, -1] or lst == [-1, 1]:
        return '()'
    elif cor(lst):
        return rev(lst)
    ans = ''
    for i in range(2, len(lst)+1):
        if bal(lst[:i]):
            if cor(lst[:i]):
                return rev(lst[:i]) + sep(lst[i:])
            else:
                return '(' + sep(lst[i:]) + ')' + rev(list(map(lambda x: (-1)*x, lst[1:i-1])))
    return ans


def bal(lst):
    if sum(lst) == 0:
        return True
    else:
        return False


def cor(lst):
    tmp = 0
    if sum(lst) == 0:
        for _ in lst:
            tmp += _
            if tmp < 0:
                return False
        return True
    else:
        return False


def chg(p):
    tmp = []
    for _ in list(p):
        if _ == '(':
            tmp.append(1)
        else:
            tmp.append(-1)
    return tmp


def rev(lst):
    tmp = ''
    for _ in lst:
        if _ == 1:
            tmp += '('
        else:
            tmp += ')'
    return tmp
