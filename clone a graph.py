# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def enqueue(self, node):
        self.queue = [node] + self.queue
        self.size += 1
        
    def dequeue(self):
        self.size -= 1
        return self.queue.pop()
    
    def is_not_empty(self):
        return bool(self.size)
        
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.queue = Queue()
        self.copies = {}
        
    def cloneGraph(self, node):
        clone_node_root = UndirectedGraphNode(node.label)
        self.copies[node] = clone_node_root
        self.queue.enqueue(node)
        while self.queue.is_not_empty():
            current_node = self.queue.dequeue()
            for neighbor in current_node.neighbors:
                if neighbor not in self.copies:
                    self.queue.enqueue(neighbor)
                    clone_node = UndirectedGraphNode(neighbor.label)
                    self.copies[neighbor] = clone_node
                self.copies[current_node].neighbors.append(self.copies[neighbor])
        return clone_node_root