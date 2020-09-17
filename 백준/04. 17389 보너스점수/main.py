N, A = input(), list(input())

total_sco = 0
bonus = 0
tmp = -1

for idx, ans in enumerate(A):
    if ans == 'O':
        tmp += 1
        total_sco += idx+1
        bonus += tmp

    else:
        total_sco += bonus
        tmp = -1
        bonus = 0
total_sco += bonus

print(total_sco)
