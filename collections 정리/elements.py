import collections
c = collections.Counter("Hello Python")
print(list(c.elements()))
print(sorted(c.elements()))
'''
결과
['n', 'h', 'l', 'l', 't', 'H', 'e', 'o', 'o', ' ', 'y', 'P']
[' ', 'H', 'P', 'e', 'h', 'l', 'l', 'n', 'o', 'o', 't', 'y']
'''
c2 = collections.Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
'''
결과
['a', 'a', 'a', 'a', 'b', 'b']
'''
