def insertion_sort(lst):
    for st in range(1, len(lst)):
        idx = st
        for i in range(st-1, -1, -1):
            if lst[i] > lst[idx]:
                lst[i], lst[idx] = lst[idx], lst[i]
                idx = i
            else:
                break
    return lst
