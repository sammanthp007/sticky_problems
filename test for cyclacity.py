def test_for_cyclicity(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr != None:
        slow = slow.next
        if slow is fast:
            return True
        if fast.next != None:
            fast = fast.next.next
        else:
            return False
        if fast is slow:
            return True
    return False