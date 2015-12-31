class NodeType(object):
    def __init__(self, data=""):
        self.data = data
        self.next = None

def merge_two_sorted_liste(head1, head2):
    temp_head = NodeType(0)
    temp_ptr = temp_head
    while head1 or head2:
        if head1 and head2:
            if head1.data < head2.data:
                temp_ptr.next = head1
                head1 = head1.next
            else:
                temp_ptr.next = head2
                head2 = head2.next
            temp_ptr = temp_ptr.next
        elif head1:
            temp_ptr.next = head1
            head1 = head1.next
            temp_ptr = temp_ptr.next
        elif head2:
            temp_ptr.next = head2
            head2 = head2.next
            temp_ptr = temp_ptr.next
    temp_head = temp_head.next
    return temp_head
