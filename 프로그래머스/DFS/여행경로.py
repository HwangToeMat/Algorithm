ans = []


def solution(tickets):
    global ans
    for _ in range(len(tickets)):
        if tickets[_][0] == "ICN":
            ck = [0 for _ in range(len(tickets))]
            answer = ['ICN']
            answer.append(tickets[_][1])
            dfs(ck, answer, tickets, _)
    return sorted(ans, key=lambda x: ''.join(x), reverse=True)[-1]


def dfs(ck, answer, tickets, idx):
    global ans
    ck[idx] = 1
    if len(answer) == len(tickets) + 1:
        tmp = []
        for _ in answer:
            tmp.append(_)
        ans.append(tmp)
        return
    for _ in range(len(tickets)):
        if ck[_] or tickets[idx][1] != tickets[_][0]:
            continue
        ck[_] = 1
        answer.append(tickets[_][1])
        dfs(ck, answer, tickets, _)
        answer.pop()
        ck[_] = 0
    return
