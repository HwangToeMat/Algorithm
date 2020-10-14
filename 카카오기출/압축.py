def solution(msg):
    answer = []
    alp = {chr(_): _ - 64 for _ in range(65, 91)}
    idx, cnt = 0, 27
    while True:
        k = 1
        while alp.get(msg[idx:idx+k]) != None:
            if idx+k > len(msg):
                answer.append(alp[msg[idx:idx+k-1]])
                return answer
            k += 1
        alp[msg[idx:idx+k]] = cnt
        cnt += 1
        answer.append(alp[msg[idx:idx+k-1]])
        idx = idx+k-1
        if idx >= len(msg):
            break
