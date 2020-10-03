def solution(arrows):
    s = [[0, 0]]
    answer = 0
    route = set(())
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
        rev = tuple([tuple(tmp[0]), tuple(tmp[1]), tuple(tmp[2])])
        rev1 = tuple([tuple(tmp[2]), tuple(tmp[1]), tuple(tmp[0])])
        if rev in route or rev1 in route:
            continue
        else:
            if rev[2] in visit and rev[1] in visit:
                answer += 2
            elif rev[2] in visit or rev[1] in visit:
                answer += 1
            else:
                answer += 0
            route.add(rev)
            for t in rev:
                if t not in visit:
                    visit.add(t)
    return answer


def mv(num, s):
    m = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    x = s[-1][0] + m[num][0]
    y = s[-1][1] + m[num][1]
    s.append([x, y])
