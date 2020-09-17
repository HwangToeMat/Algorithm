def solution(operations):
    answer = []
    for _ in operations:
        tmp = _.split()
        if tmp[0] == 'I':
            m = int(tmp[-1])
            answer.append(m)
        elif tmp[0] == 'D':
            if answer == []:
                continue
            if tmp[1] == '1':
                m = max(answer)
                answer.remove(m)
            else:
                m = min(answer)
                answer.remove(m)
    if answer == []:
        ans = [0, 0]
    else:
        ans = []
        ans.append(max(answer))
        ans.append(min(answer))

    return ans
