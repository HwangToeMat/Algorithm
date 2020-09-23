import collections


def solution(s):
    answer = []

    lst = s.replace('{', '').replace('}', '').replace(',', '|').split('|')

    container = collections.Counter()
    container.update(lst)
    tmp = sorted(container.items(), key=lambda x: x[1], reverse=True)
    answer = list(map(lambda x: int(x[0]), tmp))
    return answer
