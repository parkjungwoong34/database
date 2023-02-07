import os
class Tree() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None

memory = []
root = None
adressesAry = []

folderName = 'C:/Program Files/Common Files/'
for dirName, subDirList, fnames in os.walk(folderName) :
	for fname in fnames :
		adressesAry.append(fname)

node = Tree()
node.data = adressesAry[0]
root = node
memory.append(node)

dupNameAry = []

for name in adressesAry[1:] :

	node = Tree()
	node.data = name

	current = root
	while True :
		if name == current.data :
			dupNameAry.append(name)
			break
		if name < current.data :
			if current.left == None :
				current.left = node
				memory.append(node)
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				memory.append(node)
				break
			current = current.right

dupNameAry = list(set(dupNameAry))

print(folderName, '및 그 하위 디렉터리의 중복된 파일 목록 -->')
print(dupNameAry)
