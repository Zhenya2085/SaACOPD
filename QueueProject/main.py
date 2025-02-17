from QueueClass import Queue

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue)  # Queue(10, 20, 30)

print(queue.dequeue())  # 10
print(queue.peek())  # 20

print(queue.size())  # 2

print(queue.is_empty())  # False
