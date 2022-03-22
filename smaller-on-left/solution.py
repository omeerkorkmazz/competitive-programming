import bisect


def Smallestonleft(arr,  n):
    sorted_arr = []
    results = []

    for i in range(0, n):
        bisect.insort(sorted_arr, arr[i])

        left_index = bisect.bisect_left(sorted_arr, arr[i])
        if left_index == 0:
            results.append(-1)
        else:
            results.append(sorted_arr[left_index-1])

    return results


if __name__ == '__main__':
    arr = [3, 5, 1, 32032, 4, 53, 12, 564, 75]
    n = len(arr)
    results = Smallestonleft(arr,n)
    print(results)

