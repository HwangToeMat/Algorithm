T = int(input())

for _ in range(T):
    N, C = int(input()), list(map(lambda x: x + 1 if x %
                                  2 != 0 else x, list(map(int, input().split()))))
    count = 0
    while True:
        if len(set(C)) == 1:
            break
        temp = C.copy()
        for n in range(N):
            C[n] = (temp[n] + temp[n-1])/2
        C = list(map(lambda x: x + 1 if x % 2 != 0 else x, C))
        count += 1
    print(count)
