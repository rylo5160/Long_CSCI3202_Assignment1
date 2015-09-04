#!/usr/bin/env python

class queue:
	def _init_(self):
		self.head = 0
		self.tail = 0
		self.n = 0
		self.l = []

	def enqueue(self, item):
		if type(item) is not int:
			return False
		self.append(item)
		self.tail += 1
		self.n += 1
		return True
		
	def dequeue(self):
		if type(item) is not int:
			return False
		if self.n = 0:
			return None
		self.head += 1
		self.n += 1
		return self.l[self.head]
		
	def size(self):
		return self.n
		
class stack:
	def _init_(self):
		self.item = []
		
	def push(self, item)
		if type(item) is not int:
			return False
		self.items.append(item)
		return True
		
	def pop(self)
		if len(self.item) == 0:
			return None
		return self.item.pop()
		
	def checkSize(self):
		return len(self.item)

class treeNode:
	def _init_(self, value, parent):
		self.key = value
		self.lChild = None
		self.rChild = None
		self.parent = parent

class binaryTree:
	def _init_(self):
		self.root = treeNode(value, None)
		
	def search(self, value, node = None):
		if node is None:
			node = self.root
		if node.key == value:
			return node
		else:
			if node.lChild is not None:
				lC = self.find(value, node.lChild)
					return lC
			if node.rChild is not None:
				rC = self.find(value, node.rChild)
					return rC
			return None
		
	def add(self, value, parentValue):
		node = self.search(parentValue)
		if node is None:
			print ("Parent not found")
			return False
		if node.lChild is not None:
			print ("Parent has two children, node not added")
			return False
		if node.rChild is not None:
			print ("Parent has two children, node not added")
			return False
		if node.lChild is None:
			node.lChild = treeNode(value, node)	#nothing here so use above class to add new node as root
			return True
		if node rChild is None:
			node.rChild = treeNode(value, node)	#same as left child
			return True
		
	def delete(value):
		node = self.search(value)
		if node is None:
			print ("Node not found.")
			return False
		if node.lChild is not None:
			print ("Node not deleted, has children")
			return False
		if node.rChild is not None:
			print ("Node not deleted, has children")
			return False
		parentNode = node.parent
		if parentNode.lChild.key == value:
			parentNode.lChild = None	#sets node to no value
		if parentNode.rChild.key == value:
			parentNode.rChild = None	#sets node ot no value
		node = None
		return True
		
	def treePrint(self, node):
		node = None
		if node is None:
			node = self.root
		return None
		if node.lChild is not None:
			tP = self.treePrint(node.lChild)
		if node.rChild is not None:
			tP = self.treePrint(node.rChild)
		return tP
			
class graph:
	def _init_ (self):
		self.values = {}
		
	def addVertex(self, value):
		if value in self.value:
			print ("vertex already exists")
			return False
		if value not in self.value:
			self.values[value] = {}
			return True
			
	def addEdge(value1, value2):
		if value1 is not in self.values or value2 is not in self.values:
			print ("One or more vertices not found.")
			return False
		else:
			self.values[value1].append[value2]
			return True
		
	def findVertex(value):
		if value in self.values:
			print self.values[value]
			return self.values[value]
		else:
			return None
