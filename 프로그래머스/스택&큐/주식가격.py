def solution(prices):
    answer = []
    for p in range(len(prices)-1):
        cnt = 0
        for t in range(p+1, len(prices)):
            cnt += 1
            if prices[p] > prices[t]:
                answer.append(cnt)
                break
        if len(answer) != p+1:
            answer.append(cnt)
    answer.append(0)
    return answer
