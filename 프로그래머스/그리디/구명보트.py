def solution(people, limit):
    answer = 0
    tmp = 0
    people.sort()
    L = len(people)
    fin = False
    for p in range(len(people)):
        if people[p] * 2 > limit:
            tmp = p
            break
        for i in range(len(people)-1, p-1, -1):
            if i == p:
                tmp = p
                fin = True
                break
            elif people[p] + people[i] <= limit:
                people[i] = people[p] + people[i]
                break
            else:
                people.pop()
        if fin:
            break
    answer = L - tmp
    return answer
