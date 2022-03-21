
def countNumberOfSubarrays(arr, k):

    counter = 0
    sum = 0

    arr_dict = {}
    arr_dict.setdefault(0, []).append(-1)

    for index in range(len(arr)):

        sum += arr[index]

        if (sum - k) in arr_dict:
            counter += len(arr_dict.get(sum - k))

        arr_dict.setdefault(sum, []).append(index)

    return counter


if __name__ == '__main__':
    arr = []
    k = 1

    for i in range(0, 58458):
        if i % 2 == 0:
            arr.append(1)
        else:
            arr.append(-1)

    result = countNumberOfSubarrays(arr, k)
    print(result)
