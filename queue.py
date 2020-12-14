from collections import deque #덱을 이용해라!

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
queue.append(5)
queue.popleft()

print(queue) # 먼저들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터