from BinaryTreeClass import BinaryTree

# Создаем бинарное дерево
tree = BinaryTree()

# Вставляем элементы
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

# Вывод дерева (обход in-order)
print("In-order:", tree.inorder())  # [20, 30, 40, 50, 60, 70, 80]

# Обход дерева в порядке pre-order
print("Pre-order:", tree.preorder())  # [50, 30, 20, 40, 70, 60, 80]

# Обход дерева в порядке post-order
print("Post-order:", tree.postorder())  # [20, 40, 30, 60, 80, 70, 50]

# Поиск элемента
found_node = tree.find(40)
if found_node:
    print(f"Found node: {found_node.data}")  # Found node: 40
else:
    print("Node not found.")
