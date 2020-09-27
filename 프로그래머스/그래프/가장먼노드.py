import heapq
import collections


def solution(n, edge):
    answer = 0
    graph = {}
    for i in range(n):
        graph[i+1] = {}
    for a, b in edge:
        graph[a][b] = 1
        graph[b][a] = 1
    dis = dijkstra(graph, 1)
    tmp = list(dis.values())
    tmp_max = max(tmp)
    answer = dict(collections.Counter(tmp))[tmp_max]
    return answer


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
