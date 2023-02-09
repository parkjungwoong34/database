def score_Sort(ary) :
	n = len(ary)
	for end in range(1, n) :
		for cur in range(end, 0, -1) :
			if ( ary[cur-1][1] > ary[cur][1] ) :
				ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
	return ary


Score_Ary = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]


print('정렬 전 -->', Score_Ary)
Score_Ary = score_Sort(Score_Ary)
print('정렬 후 -->', Score_Ary)

print(' 성적별 조 편성표 ')
for i in range(len(Score_Ary) // 2) :
	print(Score_Ary[i][0], ':', Score_Ary[len(Score_Ary) - 1 - i][0])
