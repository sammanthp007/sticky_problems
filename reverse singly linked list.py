# reverse a singly linked list
# nodeType:
class nodeType(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list_recursion(node):
    if node.next == None:
        return node
    temp1 = reverse_linked_list_recursion(node.next)
    temp2 = node.next
    temp2.next = node
    node.next = None
    return temp1

def reverse_linked_list(node):
    current = node
    prev = None
    while current:
        next_ptr = current.next
        current.next = prev
        prev = current
        current = next_ptr
    return prev

def print_linked_list(node):
    while node != None:
        print (node.data, end=' ')
        node = node.next
    print ()

a = nodeType(2)
a.next = nodeType(3)
a.next.next = nodeType(4)
a.next.next.next = nodeType(5)
b = reverse_linked_list_recursion(a)
print_linked_list(b)
c = reverse_linked_list(b)
print_linked_list(c)