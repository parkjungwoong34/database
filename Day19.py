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


ary2 = [[55, 33, 250, 44],
		 [88,  1,  67, 23],
		 [199,222, 38, 47],
		 [155,145, 20, 99]]
ary1 = []


for i in range(len(ary2)) :
	for k in range(len(ary2[i])) :
		ary1.append(ary2[i][k])

print('1차원 변경 후, 정렬 전 -->', ary1)
ary1 = selection_Sort(ary1)
print('1차원 변경 후, 정렬 후 -->', ary1)
print('중앙값 --> ', ary1[len(ary1)//2])
