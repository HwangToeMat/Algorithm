def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), reverse=True, key=lambda x: x*3))))
