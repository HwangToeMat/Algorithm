import math


def solution(N, number):
    lst = [set([N])]
    if N == number:
        return 1
    for n in range(1, 8):
        lst.append(set())
        lst[n].add(int(str(N)*(n+1)))
        kk = n+1//2
        for u in range(kk):
            for i in lst[0+u]:
                for _ in lst[n-1-u]:
                    lst[n].add(_+i)
                    lst[n].add(_-i)
                    lst[n].add(i-_)
                    lst[n].add(_*i)
                    if i != 0:
                        lst[n].add(_//i)
                    if _ != 0:
                        lst[n].add(N//_)
                    if number in lst[n]:
                        return n + 1
    return -1
