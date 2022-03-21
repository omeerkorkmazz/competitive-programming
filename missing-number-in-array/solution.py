def MissingNumber(array, n):
    array_sum = (n * (n+1))/2
    return int(array_sum - sum(array))


if __name__ == '__main__':
    numbers = [1, 2, 3, 5]
    missing_val = MissingNumber(numbers, len(numbers))
    print("Missing Val: " + str(missing_val))
