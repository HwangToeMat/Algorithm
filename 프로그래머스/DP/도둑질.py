def solution(money):
    answer = 0
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    dp2 = [0 for _ in range(len(money))]
    dp2[1] = money[1]
    for m in range(2, len(dp1)-1):
        dp1[m] = max(dp1[m-2] + money[m], dp1[m-1])
    for m in range(2, len(dp2)):
        dp2[m] = max(dp2[m-2] + money[m], dp2[m-1])
    answer = max(max(dp1), max(dp2))

    return answer
