class LinkedList:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# sample 1
# 1 -> 1 -> 3
# 2 -> 4

# 1 -> 1 -> 2 -> 3 -> 4


def sortedMerge(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead


head1 = LinkedList(1, LinkedList(1, LinkedList(3)))
head2 = LinkedList(2, LinkedList(4))

sorted_vals = sortedMerge(head1, head2)

while sorted_vals is not None:
    print(sorted_vals.data)
    sorted_vals = sorted_vals.next
