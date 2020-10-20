def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = [lst[0]]
    L, R = [], []

    for idx in range(1, len(lst)):
        if lst[idx] < pivot[0]:
            L.append(lst[idx])
        elif lst[idx] > pivot[0]:
            R.append(lst[idx])
        else:
            pivot.append(lst[idx])
    return quick_sort(L) + pivot + quick_sort(R)
