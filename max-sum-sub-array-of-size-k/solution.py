def maximumSumSubarray(arr, n, k):
    slice_sum = sum(arr[:k])
    max_sum = slice_sum

    for i in range(n - k):
        slice_sum = slice_sum - arr[i] + arr[i + k]
        max_sum = max(slice_sum, max_sum)

    return max_sum


input = [100, 200, 300, 400]
n = len(input)
k = 2

print("Result:" + str(maximumSumSubarray(input, n, k)))
