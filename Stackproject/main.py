from StackClass import Stack

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)  # Stack(10, 20, 30)

print(stack.pop())  # 30
print(stack.peek())  # 20

print(stack.size())  # 2

print(stack.is_empty())  # False