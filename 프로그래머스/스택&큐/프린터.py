def solution(priorities, location):
    answer = 0
    tmp = []
    ans = []
    for _, i in enumerate(priorities):
        tmp.append((_, i))
    while tmp != []:
        if max(priorities) == tmp[0][1]:
            ans.append(tmp[0][0])
            priorities.remove(tmp[0][1])
            tmp.pop(0)
            if ans[-1] == location:
                return len(ans)
        else:
            tmp.append(tmp[0])
            tmp.pop(0)
    return answer
