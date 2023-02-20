import random

def Bin_Search(ary, fData):
	start = 0
	end = len(ary) - 1

	while (start <= end) :
		mid = (start + end) // 2
		if fData == ary[mid] :
			return mid
		elif fData > ary[mid] :
			start = mid + 1
		else :
			end = mid - 1

	return -1

Data_Ary = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
Sell_Ary = [random.choice(Data_Ary) for _ in range(20)]

print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', Sell_Ary)
Sell_Ary.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', Sell_Ary)
sellProduct = list(set(Sell_Ary))
print('#오늘 판매된 물품 종류(중복x) -->', sellProduct)

countList = []
for product in sellProduct :
	count = 0
	pos = 0
	while (pos != -1) :
		pos = Bin_Search(Sell_Ary, product)
		if pos != -1 :
			count += 1
			del(Sell_Ary[pos])
	countList.append( (product, count))

print()
print("결산 결과 ==>", countList)
