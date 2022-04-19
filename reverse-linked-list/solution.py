def reverseList(self, head):
    cur = head
    reverse = None
        
    while cur is not None:
        temp = cur.next
        cur.next = reverse
        reverse = cur
        cur = temp
        
    return reverse