import heapq


def dijkstra(graph, start):
    dis = {node: float('inf') for node in graph}
    dis[start] = 0
    load = []
    heapq.heappush(load, [0, start])

    while load:
        new_dis, new = heapq.heappop(load)
        if new_dis <= dis[new]:
            for node, weight in graph[new].items():
                if dis[node] >= dis[new] + weight:
                    dis[node] = dis[new] + weight
                    heapq.heappush(load, [dis[node], node])
    return dis


"""
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
"""
