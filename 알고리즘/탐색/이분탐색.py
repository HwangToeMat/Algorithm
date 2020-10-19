def binary_search(lst, data):
    lst.sort()
    left, right = 0, len(lst)
    while True:
        mid = (left + right)//2
        if lst[mid] == data:
            return lst[mid]
        elif lst[mid] < data:
            left = mid + 1
        elif lst[mid] > data:
            right = mid

        if left == right:
            return False
