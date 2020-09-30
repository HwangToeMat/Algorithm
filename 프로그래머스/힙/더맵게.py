def solution(scoville, K):
    import heapq
    data = []
    for s in scoville:
        heapq.heappush(data, s)
    answer = 0
    while len(data) > 0:
        if data[0] >= K:
            return answer
        a = heapq.heappop(data)
        if data != []:
            b = heapq.heappop(data)
            heapq.heappush(data, a + (b * 2))
        answer += 1
    return -1
