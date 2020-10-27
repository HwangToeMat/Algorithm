def solution(s):
    answer = 100000
    for n in range(1, len(s)//2 + 2):
        new_wrd = process(s, n)
        answer = min(answer, len(new_wrd))
    return answer


def process(s, n):
    ret = ''
    tmp = ''
    cnt = 0
    if s[:n] != s[n: 2*n] or len(s) == 1:
        return s
    for _ in range(0, len(s) + n, n):
        if s[_: _ + n] == tmp:
            cnt += 1
        else:
            if cnt > 1:
                ret += str(cnt) + tmp
                cnt = 1
                tmp = s[_:_+n]
            else:
                cnt = 1
                ret += tmp
                tmp = s[_:_+n]
    if cnt > 1:
        ret += str(cnt) + tmp
    else:
        ret += tmp
    return ret
