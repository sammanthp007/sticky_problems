class NodeType(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next = n
    
    def get_data(self):
        return self.data
    
    def set_data(self,d):
        self.data = d
        
    def get_next(self):
        return self.next
    
    def set_next(self, n):
        self.next = n
        
class Stack(object):
    def __init__(self):
        self.head = None
        
    def push(self, d):
        new_node = NodeType(d)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data
    
    def top(self):
        return self.head.data
    
    def is_empty(self):
        if self.head == None:
            return True
        return False
    
    def print_stack(self):
        this_node = self.head
        self.print_from(this_node)
        print ()
        
    def print_from(self, node):
        if node == None:
            return
        print (node.data, end=" ")
        self.print_from(node.next)
        
        
class ArrayStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, d):
        self.stack.append(d)
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print (self.stack)
    
    
    
# a = Stack()
# a.push(2)
# a.push(43)
# a.push(23)
# a.print_stack()
# print (a.pop())
# a.print_stack()
#     