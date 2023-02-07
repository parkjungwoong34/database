
def is_queue_full() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

def is_queue_empty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def en_queue(data) :
	global SIZE, queue, front, rear
	if (is_queue_full()) :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data

def de_queue() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None

	for i in range(front + 1, rear + 1): 	# 모든 사람을 한칸씩 앞으로 당긴다.
		queue[i - 1] = queue[i]
		queue[i] = None
	front = -1
	rear -= 1

	return data

def peek() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1

if __name__ == "__main__" :
	en_queue('강호동')
	en_queue('이수근')
	en_queue('은지원')
	en_queue('김c')
	en_queue('이승기')
	print("대기 상태 : ", queue)

	for _ in range(rear+1) :
		print(de_queue(), ' 식당에 들어감')
		print("대기 상태 : ", queue)

	print("영업 종료!")
