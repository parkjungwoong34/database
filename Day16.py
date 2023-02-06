class Node2() :
	def __init__ (self) :
		self.Llink = None
		self.data = None
		self.Rlink = None

def printNodes(start):
	current = start
	if current.Rlink == None :
		return
	print("정방향 --> ", end=' ')
	print(current.data, end=' ')
	while current.Rlink != None:
		current = current.Rlink
		print(current.data, end=' ')
	print()
	print("역방향 --> ", end=' ')
	print(current.data, end=' ')
	while current.Llink != None:
		current = current.Llink
		print(current.data, end=' ')

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :

	node = Node2()
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :
		pre = node
		node = Node2()
		node.data = data
		pre.Rlink = node
		node.Llink = pre
		memory.append(node)

	printNodes(head)
