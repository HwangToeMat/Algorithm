def solution(files):
    file_lst = []
    for i, file in enumerate(files):
        lst = ['', '', '', i]
        for idx, f in enumerate(file):
            if f.isdigit():
                lst[1] += f
                if idx == len(file) - 1 or not file[idx+1].isdigit():
                    lst[2] += file[idx+1:]
                    break
            else:
                lst[0] += f
        file_lst.append(lst)
    return list(map(lambda x: ''.join(x[:3]), sorted(file_lst, key=lambda x: (x[0].upper(), int(x[1]), x[3]))))
