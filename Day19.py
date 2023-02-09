## 함수 선언 부분 ##
def Nota(base, n):
	if n < base :
		print(numberCh[n], end =' ')
	else :
		Nota(base, n // base)
		print(numberCh[n % base], end =' ')

numberCh = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberCh += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('10진수 입력 -->'))
print('\n 2진수 : ', end = ' ')
Nota(2, number)
print('\n 8진수 : ', end = ' ')
Nota(8, number)
print('\n16진수 : ', end = ' ')
Nota(16, number)
