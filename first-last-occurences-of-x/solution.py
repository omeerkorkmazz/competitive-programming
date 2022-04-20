def firstAndLast(self, arr, n, x):
    min_index = -1
    max_index = -1

    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if x <= arr[mid]:
            high = mid-1
        else:
            low = mid+1

        if x == arr[mid]:
            min_index = mid

    low = 0
    high = n-1

    while low <= high:
        mid = (low+high) // 2
        if x >= arr[mid]:
            low = mid+1
        else:
            high = mid-1

        if x == arr[mid]:
            max_index = mid

    if min_index == -1:
        return [-1]
    else:
        return [min_index, max_index]
