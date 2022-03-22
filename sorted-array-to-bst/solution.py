def pre_order(nums, start, end, tree):
    if start > end:
        return

    mid = (start + end) // 2
    tree.append(nums[mid])
    pre_order(nums, start, mid-1, tree)
    pre_order(nums, mid+1, end, tree)


def sortedArrayToBST(nums):
    tree = []
    size = len(nums)
    pre_order(nums, 0, size-1, tree)
    return tree
