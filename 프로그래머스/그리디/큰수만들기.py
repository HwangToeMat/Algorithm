def solution(number, k):
    answer = ''
    lst = list(map(int, list(number)))
    idx = 0
    tmp_idx = 0
    L = len(lst)
    L_a = L - k
    if len(set(lst)) == 1:
        print(dwqq)
    while k:
        if k < 0 or idx + k + 1 > L:
            break
        tmp = 0
        for i in range(idx, idx + k + 1):
            if lst[i] == 9:
                tmp = lst[i]
                tmp_idx = i
                break
            if tmp < lst[i]:
                tmp = lst[i]
                tmp_idx = i
        k -= (tmp_idx-idx)
        idx = tmp_idx + 1
        answer += str(tmp)
        if len(answer) == L_a:
            return answer
    if len(answer) != L_a:
        answer += number[idx:]
    return answer
