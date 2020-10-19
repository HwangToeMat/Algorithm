def selection_sort(lst):
    for st in range(len(lst)-1):
        select = False
        tmp = st
        for idx in range(st+1, len(lst)):
            if lst[tmp] > lst[idx]:
                tmp = idx
                select = True
        if select:
            lst[st], lst[tmp] = lst[tmp], lst[st]
    return lst
