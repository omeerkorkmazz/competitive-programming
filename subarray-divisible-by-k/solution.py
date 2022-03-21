def kSub(k, nums):
    counter = 0

    mods = []

    for i in range(0, k):
        mods.append(0)

    mods[0] += 1
    calc = 0
    for j in range(0, len(nums)):
        calc = ((calc + nums[j]) % k + k) % k
        counter += mods[calc]
        mods[calc] += 1

    return counter


if __name__ == '__main__':
    counter = kSub(5, [1, 2, 3, 4, 5])
    print(counter)
