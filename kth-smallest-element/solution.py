def kthSmallest(arr, start, end, k):
    arr.sort()
    return arr[k-1]

if __name__ == '__main__':
    numbers = [1, 4, 5, 10, 12, 2]
    k = 3
    start = 0
    end = len(numbers)
    print("Kth smallest element: " + str(kthSmallest(numbers, start, end, k)))
