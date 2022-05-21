def inOrder(root):
    nums = ""
    stack = []
    curr = root
    
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif(stack):
            curr = stack.pop()
            nums = nums + str(curr.info) + " "
            curr = curr.right
        else:
            break
    
    print(nums)