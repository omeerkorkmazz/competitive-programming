def detectLoop(self, head):
    fast = head
    slow = head

    while slow.next != None:
        if fast.next != None:
            if fast.next.next != None:
                fast = fast.next.next
                if fast == slow:
                    return True
                else:
                    slow = slow.next
            else:
                break
        else:
            break

    return False
