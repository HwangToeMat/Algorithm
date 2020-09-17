def solution(brown, yellow):
    answer = []
    for y in range(1, max(int(brown-6/2), yellow)+1):
        x1 = brown//2 - y - 2
        x2 = yellow/y
        if x1 == x2:
            return [x1+2, y+2]

    return answer
