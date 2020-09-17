import collections
c3 = collections.Counter('hello python')
c4 = collections.Counter('i love python')
c3.subtract(c4)
print(c3)
'''
결과
Counter({'l': 1, 'h': 1, 'n': 0, 't': 0, 'p': 0, 'e': 0, 'o': 0, 'y': 0, 'i': -1, 'v': -1, ' ': -1})
'''
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
'''
결과
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
'''
