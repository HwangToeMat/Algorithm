def solution(N, stages):
    stages.sort()
    score = {}
    for _ in range(N):
        score[_ + 1] = 0
    cnt = 0
    tmp = stages[0]
    for n in range(len(stages)):
        if tmp != stages[n]:
            score[tmp] = (n - cnt) / (len(stages) - cnt)
            cnt = n
            tmp = stages[n]
        else:
            tmp = stages[n]
    if tmp <= N:
        score[tmp] = (n - cnt + 1) / (len(stages) - cnt)
    answer = list(
        dict(sorted(score.items(), key=lambda x: x[1], reverse=True)).keys())

    return answer
