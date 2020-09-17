N, M = map(int, input().split())
team_mem = {}
mem_team = {}

for _ in range(N):
    team_name = input()
    num = int(input())
    team_mem[team_name] = []
    for i in range(num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for _ in range(M):
    Q, T = input(), int(input())
    if T:
        print(mem_team[Q])
    else:
        for _ in sorted(team_mem[Q]):
            print(_)
