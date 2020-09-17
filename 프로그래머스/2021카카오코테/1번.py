def solution(new_id):
    lst = list("~!@#$%^&*()=+[{]}:?,<>")
    answer = new_id.lower()  # 1단계
    new_id = answer
    tmp = ''  # 2단계,3단계
    for _ in range(len(new_id)):
        if new_id[_] not in lst:
            if len(tmp) != 0 and tmp[-1] == '.' and new_id[_] == '.':
                continue
            tmp += new_id[_]
    new_id = tmp.strip('.')  # 4단계
    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    elif len(new_id) <= 2:
        k = new_id[-1]
        while len(new_id) < 3:
            new_id += k

    return new_id
