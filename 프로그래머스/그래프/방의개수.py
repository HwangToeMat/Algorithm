def solution(arrows):
    s = [[0, 0]]
    answer = 0
    route = []
    visit = set(())
    for a in arrows:
        tmp = []
        tmp.append(s[-1])
        mv(a, s)
        x = (s[-1][0] + tmp[0][0]) / 2
        y = (s[-1][1] + tmp[0][1]) / 2
        t = [x, y]
        tmp.append(t)
        tmp.append(s[-1])
        rev = [tmp[2], tmp[1], tmp[0]]
        if tmp in route or rev in route:
            continue
        else:
            if tuple(tmp[2]) in visit and tuple(tmp[1]) in visit:
                answer += 2
            elif tuple(tmp[2]) in visit or tuple(tmp[1]) in visit:
                answer += 1
            else:
                answer += 0
            route.append(tmp)
            for t in tmp:
                if set(t) not in visit:
                    visit.add(tuple(t))
    return answer


def mv(num, s):
    m = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    x = s[-1][0] + m[num][0]
    y = s[-1][1] + m[num][1]
    s.append([x, y])
