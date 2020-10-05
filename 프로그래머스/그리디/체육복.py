def solution(n, lost, reserve):
    answer = n
    lost.sort()
    for l in lost:
        if l in reserve:
            continue
        elif l - 1 in reserve and l - 1 not in lost:
            reserve.remove(l-1)
        elif l + 1 in reserve and l + 1 not in lost:
            reserve.remove(l+1)
        else:
            answer -= 1
    return answer
