def solution(lines):
    answer = 0
    lst = []
    for i in lines:
        _, t, d = i.split()
        h, m, s  = t.split(':')
        tmp_t = int((int(h) * 60**2 + int(m) * 60 + float(s)) * 1000)
        tmp_d = int(float(d.rstrip('s')) * 1000)
        if tmp_d > 3000:
            tmp_d = 3000
        lst.append((tmp_t - tmp_d + 1, tmp_t))
    for st, end in lst:
        cnt_s = 0
        cnt_e = 0
        for s, e in lst:
            if not (e < st or s > st + 999):
                cnt_s += 1
            if not (e < end or s > end + 999):
                cnt_e += 1
        answer = max(cnt_s, cnt_e, answer)    
    return answer