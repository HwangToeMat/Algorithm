def solution(progresses, speeds):
    answer = []
    while True:
        cnt = []
        while True:
            if progresses[0] >= 100:
                tmp = progresses.pop(0)
                speeds.pop(0)
                cnt.append(tmp)
                if progresses == []:
                    answer.append(len(cnt))
                    break
            else:
                if len(cnt) != 0:
                    answer.append(len(cnt))
                break
        if progresses == []:
            break
        for _ in range(len(progresses)):
            progresses[_] += speeds[_]

    return answer
