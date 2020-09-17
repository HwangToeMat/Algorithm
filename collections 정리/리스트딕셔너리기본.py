import collections
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))
print(collections.Counter({'가': 3, '나': 2, '다': 4}))

'''
결과
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
'''
'''
결과
Counter({'다': 4, '가': 3, '나': 2})
'''