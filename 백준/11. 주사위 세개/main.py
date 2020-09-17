A = list(map(int, input().split()))

if len(set(A)) == 1:
    tmp = A[0]
    print(10000 + 1000 * tmp)
elif len(set(A)) == 2:
    tmp = sorted(A)[1]
    print(1000 + 100 * tmp)
else:
    print(100 * max(A))
