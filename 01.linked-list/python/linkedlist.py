class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	

class LinkedList:
	def __init__(self, value):
		node = Node(value)
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
		if self.indexOf(value) >= 0:
			return True
		return False

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

