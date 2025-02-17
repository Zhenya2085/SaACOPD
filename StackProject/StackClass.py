class Stack:
    def __init__(self):                         # Инициализация пустого стека.
        self.items = []

    def is_empty(self):                         # Проверка, пуст ли стек.
        return len(self.items) == 0

    def push(self, item):                       # Добавление элемента в стек.
        self.items.append(item)

    def pop(self):                              # Удаление и возврат элемента из стека (если стек не пуст).
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("извлечение из пустого стека")

    def peek(self):                             # Возвращение верхнего элемента стека без удаления.
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("просмотр из пустого стека")

    def size(self):                             # Возвращение размера стека.
        return len(self.items)

    def __str__(self):                          # Преобразование стека в строковое представление для удобства.
        return "Stack(" + ", ".join(map(str, self.items)) + ")"