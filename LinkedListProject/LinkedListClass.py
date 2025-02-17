from Node import Node

class LinkedList:
    """Инициализация пустого списка."""
    def __init__(self):
        self.head = None  # Начало списка

    """Добавление элемента в конец списка."""
    def append(self, data):
        new_node = Node(data)  # Создаем новый узел
        if not self.head:  # Если список пуст, новый узел становится головой
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:  # Идем до последнего узла
                last_node = last_node.next
            last_node.next = new_node  # Присваиваем ссылку на новый узел

    """Добавление элемента в начало списка."""
    def prepend(self, data):
        new_node = Node(data)  # Создаем новый узел
        new_node.next = self.head  # Новый узел указывает на текущую голову
        self.head = new_node  # Новый узел становится головой списка

    """Удаление первого найденного узла с заданными данными."""
    def delete(self, data):
        current = self.head
        if current and current.data == data:  # Если удаляем первый элемент
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != data:  # Ищем узел
            prev = current
            current = current.next
        
        if current is None:  # Если элемент не найден
            return
        
        prev.next = current.next  # Удаляем узел, обновив ссылку
        current = None

    """Поиск элемента в списке."""
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    """Возвращение размера списка."""
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    """Строковое представление списка."""
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
