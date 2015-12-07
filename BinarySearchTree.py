class NodeType(object):
    def __init__(self, d=None):
        self.data = d
        self.left_child = None
        self.right_child = None
        self.next_node = None
    
class Queue(object):
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def create_node(self,d):
        return NodeType(d)
    
    def enqueue(self, node):
        if self.front == -1:
            self.rear = node
            self.front = node
        else:
            self.rear.next_node = node
            self.rear = self.rear.next_node
        self.size += 1
    
    def dequeue(self):
        if self.front == -1:
            return False
        elif self.rear == self.front:
            pop_value = self.front
            self.front = -1
            self.rear = -1
            self.size -= 1
            return pop_value
        else:
            pop_value = self.front
            self.front = self.front.next_node
            self.size -= 1
            return pop_value
    
    def print_queue(self):
        this_node = self.front
        while this_node:
            this_node = this_node.next_node

    def is_empty(self):
        return not bool(self.size)

class BinarySearchTree(object):
    def __init__(self, root = None):
        self.root = root
        
    def create_node(self, d):
        a = NodeType(d)
        return a
    
    def insert(self, d):
        this_node = self.root
        new_node = self.create_node(d)
        if self.root == None:
            self.root = new_node
        else:
            self.insert_starting_from(this_node, new_node)
        
    def insert_starting_from(self, root, node):
        if root.data > node.data:
            if root.left_child == None:
                root.left_child = node
            else:
                self.insert_starting_from(root.left_child, node)
        else:
            if root.right_child == None:
                root.right_child = node
            else:
                self.insert_starting_from(root.right_child, node)
    
    def search(self, d):
        new_node = self.create_node(d)
        this_node = self.root
        return self.search_starting_from(this_node, new_node)
        
    def search_starting_from(self, root, node):
        if root == None:
            return False
        elif root.data == node.data:
            return node.data
        elif root.data > node.data:
            return self.search_starting_from(root.left_child, node)
        else:
            return self.search_starting_from(root.right_child, node)
        
    def remove(self, d):
        new_node = self.create_node(d)
        this_node = self.root
        if d == self.root.data:
            pass
        self.remove_starting_from(this_node, new_node)
        
    def remove_starting_from(self, root, node):
        pass
    
    
    def calculate_height_of_tree(self):
        this_node = self.root
        if this_node == None:
            return -1
        return self.calculate_height_from(this_node)
    
    def calculate_height_from(self, root):
        if not root:
            return -1
        if not root.left_child and not root.right_child:
            return 0
        height_left_child = self.calculate_height_from(root.left_child)
        height_right_child = self.calculate_height_from(root.right_child)
        print (root.data, height_left_child, height_right_child)
        if height_left_child > height_right_child:
            return 1 + height_left_child
        else:
            return 1 + height_right_child
    
    def breadth_first_traversal(self):
        if not self.root:
            return False
        else:
            queue = Queue()
            this_node = self.root
            queue.enqueue(this_node)
            while (not queue.is_empty()):
                current_node = queue.dequeue()
                if current_node.left_child:
                    queue.enqueue(current_node.left_child)
                if current_node.right_child:
                    queue.enqueue(current_node.right_child)
                print (current_node.data, end=' ')
            print ()
        
    def inorder_traversal(self):
        this_node = self.root
        self.inorder_traversal_from(this_node)
        print ()
    
    def inorder_traversal_from(self, root):
        if not root:
            return
        self.inorder_traversal_from(root.left_child)
        print (root.data, end=' ')
        self.inorder_traversal_from(root.right_child)
            
    def postorder_traversal(self):
        this_node = self.root
        self.postorder_traversal_from(this_node)
        print ()
        
    def postorder_traversal_from(self, root):
        if root == None:
            return
        self.postorder_traversal_from(root.left_child)
        self.postorder_traversal_from(root.right_child)
        print (root.data, end=' ')
        
    def preorder_traversal(self):
        this_node = self.root
        self.preorder_traversal_from(this_node)
        print ()
        
    def preorder_traversal_from(self, root):
        if root == None:
            return
        print (root.data, end=' ')
        self.preorder_traversal_from(root.left_child)
        self.preorder_traversal_from(root.right_child)
    
    def goldman_sachs_traversal(self):
        this_node = self.root
        self.goldman_traversal_from(this_node)
        print ()

    def goldman_traversal_from(self, root):
        stack = Stack()
        queue = Queue()
        queue.enqueue(root)
        while queue.size:
            front = queue.dequeue()
            if front.right_child:
                queue.enqueue(front.right_child)
            if front.left_child:
                queue.enqueue(front.left_child)
            # print ('>>',front.data)
            stack.push(front)
            # print (stack)
        while stack.size:
            res = stack.pop()
            print (res.data, end=' ')

def is_bst(root):
    return check_is_bst(root, float('inf'), float('-inf'))

def check_is_bst(root, max_val, min_val):
    if root == None :
        return True
    if root.data <= max_val and root.data > min_val and is_bst(root.left_child, root.data, min_val) and is_bst(root.right_child, max_val, root.data):
        return True
    return False


class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, d):
        new_node = NodeType(d)
        new_node.next_node = self.head
        self.head = new_node
        self.size += 1
        # print (self.head.data)

    def pop(self):
        pop_data = self.head.data
        self.head = self.head.next_node
        # print (self.head.data)
        self.size -= 1
        return pop_data

    def peek(self):
        return self.head.data


# b = BinarySearchTree()
# b.insert(15)
# b.insert(5)
# b.insert(16)
# b.insert(3)
# b.insert(12)
# b.insert(10)
# b.insert(13)
# b.insert(6)
# b.insert(7)
# b.insert(20)
# b.insert(18)
# b.insert(23)
# b.breadth_first_traversal()
# b.goldman_sachs_traversal()
# b.inorder_traversal()
# b.postorder_traversal()
# b.preorder_traversal()
# print (b.root.left_child.data)
# print (b.root.right_child.data)
# print (b.root.right_child.right_child.data)
# print (b.root.left_child.right_child.right_child.data)
# print (b.root.left_child.left_child)
# print (b.calculate_height_of_tree())   