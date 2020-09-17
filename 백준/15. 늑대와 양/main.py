R, C = map(int, input().split())

A = [list(input()) for _ in range(R)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
ans = 1

for r in range(R):
    for c in range(C):
        if A[r][c] == 'W':
            for _ in range(4):
                if r + dx[_] >= 0 and r + dx[_] < R and c + dy[_] >= 0 and c + dy[_] < C:
                    if A[r + dx[_]][c + dy[_]] == 'S':
                        ans = 0
                        break
                    else:
                        if A[r + dx[_]][c + dy[_]] == '.':
                            A[r + dx[_]][c + dy[_]] = 'D'
                else:
                    continue

print(ans)
if ans == 1:
    for _ in range(R):
        print(''.join(A[_]))
