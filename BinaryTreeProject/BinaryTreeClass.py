from Node import Node

class BinaryTree:
    def __init__(self):     # Инициализация пустого бинарного дерева.
        self.root = None

    def insert(self, data):     # Вставка нового элемента в дерево.
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):    # Рекурсивная вставка элемента в правильное место в дереве.
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def find(self, data):       # Поиск элемента в дереве.
        return self._find_recursive(self.root, data)

    def _find_recursive(self, node, data):      # Рекурсивный поиск элемента в дереве.
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self._find_recursive(node.left, data)
        else:
            return self._find_recursive(node.right, data)

    def inorder(self):      # Обход дерева в порядке "левый-узел-правый" (in-order).
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):     # Рекурсивный обход дерева в порядке in-order.
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.data] + self._inorder_recursive(node.right)

    def preorder(self):     # Обход дерева в порядке "узел-левый-правый" (pre-order).
        return self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):        # Рекурсивный обход дерева в порядке pre-order.
        if node is None:
            return []
        return [node.data] + self._preorder_recursive(node.left) + self._preorder_recursive(node.right)

    def postorder(self):        # Обход дерева в порядке "левый-правый-узел" (post-order). 
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):       # Рекурсивный обход дерева в порядке post-order.
        if node is None:
            return []
        return self._postorder_recursive(node.left) + self._postorder_recursive(node.right) + [node.data]

    def __str__(self):      # Строковое представление дерева.
        return " -> ".join(map(str, self.inorder()))
