import random
class TreeNode() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None

## 전역 변수 선언 부분 ##
memory = []
root = None
dataAry = ['김밥', '참치김밥', '김치김밥', '치킨마요김밥',  '깻잎김밥', '삼겹살김발' ,'삼각김밥']
sellAry = [ random.choice(dataAry) for _ in  range(20)]

print('오늘 판매된 물건(중복O) -->', sellAry)

## 메인 코드 부분 ##
node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:] :

	node = TreeNode()
	node.data = name

	current = root
	while True :
		if name == current.data :
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

print("이진 탐색 트리 구성 완료!")

def preorder(node) :
	if node == None :
		return
	print(node.data, end = ' ')
	preorder(node.left)
	preorder(node.right)

print('오늘 판매된 종류(중복X)--> ', end = ' ')
preorder(root)
