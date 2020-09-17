L, N = list(map(int, input().split())), input().split()

line = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
        'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
        'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
        'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
        'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

sum_name = []
ans = []
tmp = 0
finish_0 = False
finish_1 = False

# 1. input 된 값을 교차로 합치기

while True:
    if tmp < L[0]:
        alp = N[0][tmp]
        sum_name.append(line[alp])
    else:
        finish_0 = True

    if tmp < L[1]:
        alp = N[1][tmp]
        sum_name.append(line[alp])
    else:
        finish_1 = True

    if finish_0 and finish_1:
        break
    else:
        tmp += 1

while True:
    tmp_score = []
    for _ in range(1, len(sum_name)):
        temp = sum_name[_-1] + sum_name[_]
        tmp_score.append(temp % 10)

    sum_name = tmp_score
    if len(sum_name) == 2:
        break

print(str(int(''.join(list(map(str, sum_name))))) + '%')
