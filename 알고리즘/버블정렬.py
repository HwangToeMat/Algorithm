def bubblesort(lst):
    for end in range(len(lst)-1, -1, -1):
        swap = False
        for idx in range(end):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                swap = True
        if not swap:
            break
    return lst
