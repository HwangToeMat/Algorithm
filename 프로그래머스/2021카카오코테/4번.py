import heapq


def solution(n, s, a, b, fares):
    graph = fare2gra(fares)
    S = dijkstra(graph, s)
    A = dijkstra(graph, a)
    B = dijkstra(graph, b)
    tmp = []
    for i in S.keys():
        tmp.append(A[i] + B[i] + S[i])
    answer = min(A[s] + B[s], min(tmp))
    return answer


def fare2gra(fares):
    mygraph = {}
    for f in fares:
        mygraph[f[0]] = {}
        mygraph[f[1]] = {}
    for f in fares:
        mygraph[f[0]][f[1]] = f[2]
        mygraph[f[1]][f[0]] = f[2]
    return mygraph


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
