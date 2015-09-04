import unittest

class testQueue(unittest.testCase):
	def testEnQueue(self):
		q = queue()
		self.assertTrue(q.enQueue(0))
		self.assertTrue(q.enQueue(7))
		self.assertTrue(q.enQueue(-4))
		self.assertTrue(q.enQueue(34))
		self.assertTrue(q.enQueue(-100))
		self.assertTrue(q.enQueue(10000))
		self.assertTrue(q.enQueue('test'))
		self.assertTrue(q.enQueue([5,5]))
		
	def testDeQueue(self):
		q = queue()
		self.assertIsNone(q.enQueue())
		for x in xrange(0, 10):
			q.enQueue(x)
		
	def testSize(self):
		q = queue()
		
class testStack(unittest.testCase):
	def testPush(self):
		s = stack()
		self.assertTrue(s.push(0))
		self.assertTrue(s.push(1))
		self.assertTrue(s.push(-5))
		self.assertTrue(s.push(15))
		self.assertTrue(s.push(20000))
		
	def testPop(self):
		self.assertFalst(s.pop())
		for x in xrange(0, 10):
			s.push(x)
		
	def testCheckSize(self):
		s = stack()
		
class testBinaryTree(unittest, testCase):
	def testAdd(self):
		root = 10
		tN = treeNode(root)
		self.assertTrue(tN.add(17, root))
		self.assertTrue(tN.add(3, root))
		self.assertTrue(tN.add(6, 17))
		self.assertTrue(tN.add(9, 3))
		self.assertTrue(tN.add(20, root))
		self.assertTrue(tN.add(root, 9))
	
	def testDelete(self):
		tN = treeNode(1)	#1 = true?
		self.assertTrue(tN.delete(17))
		self.assertTrue(tN.delete(16))
		self.assertTrue(tN.delete(15))
		self.assertTrue(tN.delete(14))
		self.assertTrue(tN.delete(5))
		self.assertTrue(tN.delete(4))
		self.assertTrue(tN.delete(3))
		
	def testTreePrint(self):
		tN = treeNode(1)
