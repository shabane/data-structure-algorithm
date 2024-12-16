class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	

class LinkedList:
	def __init__(self, value = None):
		node = Node(value) if value else None
		self.first = node
		self.last = node
	
	def append(self, value):
		node = Node(value)
		if not self.first:
			self.first = node
			self.last = node
		else:
			self.last.next = node
			self.last = node
	
	def indexOf(self, value) -> int:
		node = self.first
		counter = -1
		while node:
			counter += 1
			if node.value == value:
				return counter
			node = node.next
		return -1

	def contains(self, value) -> bool:
		#if self.indexOf(value) >= 0:
		#	return True
		#return False
		return self.indexOf(value) != -1

	def addFirst(self, value):
		node = Node(value)
		node.next = self.first
		self.first = node

	def length(self) -> int:
		node = self.first
		counter = 0
		while node:
			counter += 1
			node = node.next
		return counter

	def removeLast(self):
		value = None
		if self.first.next is None:
			value = self.first.value
			self.first.value = None
		node = self.first
		while node:
			if node.next == self.last:
				value = node.next.value
				node.next = None
				self.last = node
				break
			node = node.next
		return value
	
	def deleteFirst(self):
		node2 = self.first.next
		del(self.first)
		self.first = node2

	def print(self):
		node = self.first
		while node:
			print(node.value)
			node = node.next
	
	def revrse(self):
		perv = self.first
		cur = perv.next
		while cur:
			next = cur.next
			cur.next = perv
			perv = cur
			cur = next

		self.last, self.first = self.first, self.last
		self.last.next = None

	def kThFromEnd(self, index):
		node = self.first
		index = self.length()-index
		for i in range(index):
			node = node.next
		return node.value
		
if __name__ == '__main__':
	linkedlist = LinkedList(12)
	linkedlist.append(13)
	linkedlist.append(14)
	linkedlist.append(15)
	print(linkedlist.indexOf(14))
	print(linkedlist.indexOf(16))
	print(linkedlist.contains(12))
	print(linkedlist.contains(10))
	linkedlist.addFirst(10)
	print(linkedlist.contains(10))
	print(linkedlist.length())
	linkedlist.append(99)
	linkedlist.removeLast()
	print("---", linkedlist.contains(99))
	print(linkedlist.contains(10))
	linkedlist.deleteFirst()
	print(linkedlist.contains(10))
	
	linkedlist.print()
	print("---")
	linkedlist.removeLast()
	linkedlist.print()
	print("---")
	linkedlist.append(15)
	linkedlist.print()
	print("---")
	linkedlist.revrse();
	linkedlist.print()
	print("---")

	print(linkedlist.kThFromEnd(3))
