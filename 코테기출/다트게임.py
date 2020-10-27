def solution(dartResult):
    cnt = 0
    tmp = 0
    answer = []
    lst = list(dartResult)
    for _ in lst:
        if cnt == 0:
            tmp += int(_)
            cnt = 1
        elif cnt == 1:
            if _ == 'D':
                tmp = tmp**2
                cnt = 2
            elif _ == 'T':
                tmp = tmp**3
                cnt = 2
            elif _ == '0':
                tmp *= 10
                cnt = 1
            else:
                cnt = 2
        else:
            if _ == '#':
                tmp *= (-1)
                answer.append(tmp)
                tmp = 0
                cnt = 0
            elif _ == '*':
                tmp *= 2
                if len(answer) == 0:
                    answer.append(tmp)
                    tmp = 0
                    cnt = 0
                    continue
                t = answer[-1]
                answer[-1] = t * 2
                answer.append(tmp)
                tmp = 0
                cnt = 0
            else:
                answer.append(tmp)
                tmp = 0
                tmp += int(_)
                cnt = 1
    answer.append(tmp)
    return sum(answer)
