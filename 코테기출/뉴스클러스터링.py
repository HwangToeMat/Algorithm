import collections
import math


def solution(str1, str2):
    answer = 0
    tmp1 = mk_set(str1)
    tmp2 = mk_set(str2)
    if tmp1 == [] and tmp2 == []:
        return 65536
    elif tmp1 == [] or tmp2 == []:
        return 0
    a = collections.Counter(tmp1)
    b = collections.Counter(tmp2)
    s_uni = a | b  # 합집합
    i_uni = a & b  # 교집합
    answer = math.trunc((sum(i_uni.values()) / sum(s_uni.values())) * 65536)
    return answer


def mk_set(st):
    tmp = []
    for i in range(len(st)-1):
        if ord(st[i]) < 65 or ord(st[i]) > 122 or (ord(st[i]) >= 91 and ord(st[i]) <= 96):
            continue
        if ord(st[i+1]) < 65 or ord(st[i+1]) > 122 or (ord(st[i+1]) >= 91 and ord(st[i+1]) <= 96):
            continue
        tmp.append(st[i:i+2].upper())
    return tmp
