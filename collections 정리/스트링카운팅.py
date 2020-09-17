import collections
container = collections.Counter()
container.update("aabcdeffgfgaccaa")
print(container)
for k, v in container.items():
    print(k, ':', v)

'''
Counter({'a': 5, 'c': 3, 'f': 3, 'g': 2, 'b': 1, 'd': 1, 'e': 1})
a : 5
b : 1
c : 3
d : 1
e : 1
f : 3
g : 2
'''
