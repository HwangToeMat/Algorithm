import collections
a = collections.Counter(['a', 'b', 'c', 'b', 'd', 'a'])
b = collections.Counter('aaeroplane')
print(a)
print(b)
print(a+b)
'''
결과
Counter({'b': 2, 'a': 2, 'd': 1, 'c': 1})
Counter({'a': 3, 'e': 2, 'n': 1, 'r': 1, 'o': 1, 'p': 1, 'l': 1})
Counter({'a': 5, 'b': 2, 'e': 2, 'n': 1, 'l': 1, 'd': 1, 'r': 1, 'o': 1, 'p': 1, 'c': 1})
'''

a = collections.Counter('aabbccdd')
b = collections.Counter('abbbce')
print(a-b)
'''
결과
Counter({'d': 2, 'c': 1, 'b': 1, 'a': 1})
'''

a = collections.Counter('aabbccdd')
b = collections.Counter('aabbbce')
print(a & b)  # 교집합
'''
결과
Counter({'b': 2, 'a': 2, 'c': 1})
'''
print(a | b)  # 합집합
'''
결과
Counter({'b': 3, 'c': 2, 'd': 2, 'a': 2, 'e': 1})
'''
