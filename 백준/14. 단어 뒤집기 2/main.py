A, tmp = input(), ''

ck = False
ans = ''

for _ in A:
    if _ == '<':
        ans += tmp[::-1]
        ans += '<'
        ck = True
        tmp = ''
    elif _ == '>':
        ans += '>'
        ck = False
    elif _ == ' ':
        if not ck:
            ans += tmp[::-1]
            tmp = ''
        ans += ' '
    else:
        if ck:
            ans += _
        else:
            tmp += _
ans += tmp[::-1]
print(ans)
