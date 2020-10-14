def solution(n, t, m, p):
    answer, ans = '', ''
    cnt = 0
    while True:
        tmp = convert(cnt, n)
        answer += tmp
        if len(answer) >= m*t:
            answer = answer[:m*t]
            break
        cnt += 1
    for mm in range(p-1, len(answer), m):
        ans += answer[mm]
    return ans


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
