import collections
c2 = collections.Counter('apple, orange, grape')
print(c2.most_common())
print(c2.most_common(2))
'''
결과
[('a', 3), ('p', 3), ('e', 3), ('g', 2), (',', 2), ('r', 2), (' ', 2), ('n', 1), ('l', 1), ('o', 1)]
[('a', 3), ('p', 3), ('e', 3)]
'''

print(str(('2', 'f')))
