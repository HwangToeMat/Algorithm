def solution(array, commands):
    answer = []
    for (i, j, k) in commands:
        if j == len(array):
            answer.append(sorted(array[i-1:])[k-1])
        else:
            answer.append(sorted(array[i-1:j])[k-1])
    return answer
