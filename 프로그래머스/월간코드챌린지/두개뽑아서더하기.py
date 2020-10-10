def solution(numbers):
    answer = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    ans = sorted(list(answer))
    return ans
