def mk_gr(graph, n):
    gr = {_: [] for _ in range(1, n+1)}
    for w, l in graph:
        if l not in gr[w]:
            gr[w].append(l)
    return gr
