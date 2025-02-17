class Queue:
    def __init__(self):                     # Инициализация пустой очереди.
        self.items = []

    def is_empty(self):                     # Проверка, пуста ли очередь.
        return len(self.items) == 0

    def enqueue(self, item):                # Добавление элемента в очередь.
        self.items.append(item)

    def dequeue(self):                      # Удаление и возврат элемента из очереди (если очередь не пуста).
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("удаление из пустой очереди")

    def peek(self):                         # Возвращение первого элемента очереди без удаления.
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("просмотр из пустой очереди")

    def size(self):                         # Возвращение размера очереди.
        return len(self.items)

    def __str__(self):                      # Преобразование очереди в строковое представление для удобства.
        return "Queue(" + ", ".join(map(str, self.items)) + ")"