def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1, a2, a3 = 0, 0, 0
    for _ in range(len(answers)):
        if s1[_ % 5] == answers[_]:
            a1 += 1
        if s2[_ % 8] == answers[_]:
            a2 += 1
        if s3[_ % 10] == answers[_]:
            a3 += 1
    lst = [a1, a2, a3]
    max_ans = max(lst)
    for _ in range(3):
        if lst[_] == max_ans:
            answer.append(_+1)

    return answer
