# This is an implementation of a binary tree in python.

class NodeType(object):
	def __init__(self):
		self.areas = 0

	def area(self, l, b):
		return l * b

	def area(self, l):
		return l ** 2

a = NodeType()
print (a.area(2,3))


