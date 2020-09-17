from itertools import permutations


def isPrime(a):
    if(a < 2):
        return False
    for i in range(2, a):
        if(a % i == 0):
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    lst = []
    for _ in range(1, len(numbers) + 1):
        lst.extend(list(map(''.join, permutations(numbers, _))))
    lst = set(map(int, lst))
    for _ in lst:
        if isPrime(_):
            answer += 1
    return answer
