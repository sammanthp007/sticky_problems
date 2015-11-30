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
        

class LinkedList(object):
    def __init__(self, head):
        self.head = NodeType(head)
        self.size = 1
                
    def insert_at_begining(self, d):
        new_node = NodeType(d, self.head)
        self.head = new_node
        self.size += 1
        
    def insert_at_end(self, d):
        new_node = NodeType(d)
        this_node = self.head
        while this_node.next != None:
            this_node = this_node.next
        this_node.set_next(new_node)
        self.size += 1
        
    def insert_at_nth(self, d, n):
        new_node = NodeType(d)
        this_node = self.head
        prev_node = None
        if self.size < n:
            return None
        for i in range(n):
            prev_node = this_node
            this_node = this_node.next
        new_node.next = this_node
        prev_node.next = new_node
    
    def get_size(self):
        return self.size
    
    def print_list(self):
        this_node = self.head
        while this_node != None:
            print (this_node.data, end=" ")
            this_node = this_node.next
        print ()
    
    def print_list_recursion(self):
        this_node = self.head
        self.print_node_recursion(this_node)
        print ()
        
    def print_node_recursion(self, node):
        if (node == None):
            return 
        print (node.data, end=" ")
        self.print_node_recursion(node.next)
        
    def reverse_print_recursion(self):
        this_node = self.head
        self.print_node_reverse_recursion(this_node)
        print ()
        
    def print_node_reverse_recursion(self, node):
        if node == None:
            return
        self.print_node_reverse_recursion(node.next)
        print (node.data, end=" ")
        
    def is_there(self, d):
        this_node = self.head
        while this_node != None:
            if this_node.data == d:
                return True
            this_node = this_node.next
        return None

    def remove(self,d):
        this_node = self.head
        while this_node != None:
            if this_node.next.data == d:
                this_node.next = this_node.next.next
                self.size -= 1
                return True
            this_node = this_node.next
        return False
                
    def reverse(self):
        this_node = self.head
        prev_node = None
        while this_node != None:
            next_node = this_node.next
            this_node.next = prev_node
            prev_node = this_node
            this_node = next_node
        self.head = prev_node

    def recursive_reverse(self):
        this_node = self.head
        self.head = self.reverse_list_starting_from(this_node)
        
    def reverse_list_starting_from(self, node):
        if node.next == None:
            self.head = node
            return
        self.reverse_list_starting_from(node.next)
        node.next.next = node
        node.next = None
    
    def add(self, n):
        this_node = self.head
        self.add_n_starting_from(this_node, n)
        
    def add_n_starting_from(self, node, n):
        if node == None:
            return
        node.data += n
        self.add_n_starting_from(node.next,n )
        
# a = LinkedList(5)
# a.insert_at_end(4)
# a.insert_at_end(9)
# a.insert_at_end(7)
# a.insert_at_end(3)
# a.print_list()
# a.reverse()
# a.print_list()
# print()
# a.reverse()
# a.print_list_recursion()
# a.reverse_print_recursion()
# a.print_list()
# a.recursive_reverse()
# a.print_list()