def getPairsCount(arr, n, k):
    count = 0
    numDict = {}

    for num in arr:
        target = k - num
        if target in numDict:
            count += numDict[target]

        if num not in numDict:
            numDict[num] = 1
        else:
            numDict[num] += 1

    return count


if __name__ == '__main__':
    numbers = [1, 5, 5, 5]
    k = 10
    n = len(numbers)
    print("Counter: " + str(getPairsCount(numbers, n, k)))
