N, A = int(input()), {i: 1 for i in list(map(int, input().split()))}
M, B = int(input()), list(map(int, input().split()))

for _ in B:
    print(A.get(_, 0))
