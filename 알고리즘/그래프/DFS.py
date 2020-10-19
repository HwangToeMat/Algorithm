def dfs(st_node, graph):
    v = [st_node]
    nv = graph[st_node]
    while len(v) != len(graph.keys()) or nv != []:
        tmp = nv.pop(-1)
        if tmp not in v:
            v.append(tmp)
            nv.extend(graph[tmp])
    return v


"""
graph
{'A': ['B', 'C'],
 'B': ['A', 'D'],
 'C': ['A', 'G', 'H', 'I'],
 'D': ['B', 'E', 'F'],
 'E': ['D'],
 'F': ['D'],
 'G': ['C'],
 'H': ['C'],
 'I': ['C', 'J'],
 'J': ['I']}

['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
"""
