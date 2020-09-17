answer = 1000000
change = False


def solution(begin, target, words):
    if target not in words:
        return 0
    ck = [0 for _ in range(len(words))]
    dfs(begin, target, words, ck)
    if not change:
        return 0
    return answer


def dfs(begin, target, words, ck):
    global answer, change
    ret = sum(ck)
    if begin == target:
        change = True
        if answer > ret:
            answer = ret
        return
    for _ in range(len(words)):
        if ck[_]:
            continue
        cnt = 0
        for i in range(len(begin)):
            if begin[i] != words[_][i]:
                cnt += 1
        if cnt == 1:
            ck[_] = 1
            dfs(words[_], target, words, ck)
            ck[_] = 0
    return
