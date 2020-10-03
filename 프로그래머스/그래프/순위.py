def solution(n, results):
    ck = True
    answer = 0
    win, lose = mk_gr(results, n)
    while ck:
        ck_w, win = update(win)
        ck_l, lose = update(lose)
        if ck_w == False and ck_l == False:
            ck = False
    for _ in range(1, n+1):
        if len(win[_]) + len(lose[_]) == n-1:
            answer += 1
    return answer


def mk_gr(graph, n):
    win = {_: [] for _ in range(1, n+1)}
    lose = {_: [] for _ in range(1, n+1)}
    for w, l in graph:
        if l not in win[w]:
            win[w].append(l)
        if w not in win[l]:
            lose[l].append(w)
    return win, lose


def update(graph):
    ck = False
    for k, v in graph.items():
        l = len(v)
        for _ in v:
            tmp = graph[_]
            for t in tmp:
                if t not in v:
                    v.append(t)
        if l != len(v):
            ck = True
    return ck, graph
