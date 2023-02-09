from tkinter import *

def Triangle(x, y, size) :
	if size >= 30 :
		Triangle(x, y, size / 2)
		Triangle(x + size / 2, y, size / 2)
		Triangle(x + size / 4, int(y - size * (3 ** 0.5) / 4), size / 2)
	else :
		canvas.create_polygon (x, y, x + size, y, x + size / 2, y - size*(3 ** 0.5) / 2, fill = 'red', outline = "red")

w_Size = 1000
radius = 400

window = Tk()
window.title("삼각형 모양의 프랙탈")
canvas = Canvas(window, height = w_Size, width = w_Size, bg ='white')

Triangle(w_Size / 5, w_Size / 5 * 4, w_Size * 2 / 3)

canvas.pack()
window.mainloop()

