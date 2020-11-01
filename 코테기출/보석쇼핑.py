def solution(gems):
    df = {}
    for idx, g in enumerate(gems, start=1):
        if df.get(g) == None:
            answer = [999999999]
        df[g] = idx
        tmp = list(df.values())
        st, end = min(tmp), idx
        dis = end - st
        if dis < answer[0]:
            answer = [dis, [st, end]]
    return answer[1]
