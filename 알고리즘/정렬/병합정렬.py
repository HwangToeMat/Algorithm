def merge_sort(lst):
    mid = len(lst)//2
    if mid <= 0:
        return lst

    L = merge_sort(lst[:mid])
    R = merge_sort(lst[mid:])

    return merge(L, R)


def merge(L, R):
    idx_l, idx_r = 0, 0
    len_l, len_r = len(L), len(R)
    merge_lst = []

    while idx_l < len_l or idx_r < len_r:
        if L[idx_l] <= R[idx_r]:
            merge_lst.append(L[idx_l])
            idx_l += 1
            if idx_l >= len_l:
                merge_lst.extend(R[idx_r:])
                break
        else:
            merge_lst.append(R[idx_r])
            idx_r += 1
            if idx_r >= len_r:
                merge_lst.extend(L[idx_l:])
                break

    return merge_lst
