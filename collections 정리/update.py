import collections
# 문자열
a = collections.Counter()
print(a)
a.update("abcdefg")
print(a)
a.update("aaahgg")
print(a)
'''
결과
Counter()
Counter({'f': 1, 'e': 1, 'b': 1, 'g': 1, 'c': 1, 'a': 1, 'd': 1})
Counter({'a': 4, 'g': 3, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'h': 1})
'''
# 딕셔너리
a.update({'f': 3, 'e': 2})
print(a)
'''
결과
Counter({'f': 4, 'e': 3, 'b': 1, 'g': 1, 'c': 1, 'a': 1, 'd': 1})
'''
