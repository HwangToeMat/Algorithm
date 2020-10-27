def solution(cacheSize, cities):
    answer = 0
    cache = [0 for _ in range(cacheSize)]
    if cacheSize == 0:
        return len(cities) * 5
    for c in cities:
        C = c.upper()
        if C not in cache:
            cache.pop(0)
            cache.append(C)
            answer += 5
        else:
            cache.remove(C)
            cache.append(C)
            answer += 1
    return answer
