import heapq

# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.


def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = str(end) + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += str(start)
    print(path_output)
    return distances


# 방향 그래프
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def fare2gra(fares):
    mygraph = {}
    for f in fares:
        mygraph[f[0]] = {}
        mygraph[f[1]] = {}
    for f in fares:
        mygraph[f[0]][f[1]] = f[2]
        mygraph[f[1]][f[0]] = f[2]
    return mygraph


mygraph = fare2gra([[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
                   5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(mygraph)
print(dijkstra(mygraph, 1, 5))

"""
{4: {1: 10, 6: 50, 2: 66}, 1: {4: 10, 3: 41, 5: 24, 6: 25}, 3: {5: 24, 1: 41, 2: 22}, 5: {3: 24, 6: 2, 1: 24}, 6: {5: 2, 4: 50, 1: 25}, 2: {4: 66, 3: 22}}
{4: 10, 3: 41, 5: 24, 6: 25}
{1: 10, 6: 50, 2: 66}
{3: 24, 6: 2, 1: 24}
{5: 2, 4: 50, 1: 25}
{5: 24, 1: 41, 2: 22}
{4: 66, 3: 22}
5->1
{4: [10, 1], 1: [0, 1], 3: [41, 1], 5: [24, 1], 6: [25, 1], 2: [63, 3]}
"""
