import random
import time

def selection_Sort(Ary) :
	n = len(Ary)
	for i in range(0, n-1) :
		minIdx = i
		for k in range(i+1, n) :
			if (Ary[minIdx] > Ary[k]) :
				minIdx = k
		tmp = Ary[i]
		Ary[i] = Ary[minIdx]
		Ary[minIdx] = tmp

	return Ary

def q_Sort(arr, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = arr[(low + high) // 2]
	while low <= high:
		while arr[low] < pivot :
			low += 1
		while arr[high] > pivot :
			high -= 1
		if low <= high :
			arr[low], arr[high] = arr[high], arr[low]
			low, high = low + 1, high - 1

	mid = low

	q_Sort(arr, start, mid - 1)
	q_Sort(arr, mid, end)

def quickSort(ary) :
	q_Sort(ary, 0, len(ary) - 1)


countAry = [1000, 10000, 12000, 15000]

for count in countAry :
	tempAry = [ random.randint(10000, 99999) for _ in range(count)]
	selectAry = tempAry[:]
	quickAry = tempAry[:]

	print("## 데이터 수 : ", count, "개")
	start = time.time()
	selection_Sort(selectAry)
	end = time.time()
	print("	선택 정렬 --> %10.3f 초" % (end-start))
	start = time.time()
	quickSort(selectAry)
	end = time.time()
	print("	퀵 정렬  --> %10.3f 초" % (end-start))
	print()

	count *= 5

