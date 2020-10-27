def solution(record):
    answer = []
    user = {}
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            user[tmp[1]] = tmp[2]
            answer.append("{}님이 들어왔습니다.".format(tmp[1]))
        elif tmp[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(tmp[1]))
        else:
            user[tmp[1]] = tmp[2]
    for idx, a in enumerate(answer):
        tmp = a.split('님')
        answer[idx] = user[tmp[0]] + '님' + tmp[1]
    return answer
