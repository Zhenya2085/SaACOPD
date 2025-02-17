class Set:
    """Инициализация пустого множества."""
    def __init__(self):
        self.items = []

    """Добавление элемента в множество, если его еще нет."""
    def add(self, element):
        if element not in self.items:
            self.items.append(element)

    """Удаление элемента из множества, если он существует."""
    def remove(self, element):
        if element in self.items:
            self.items.remove(element)
        else:
            raise ValueError(f"Элемент {element} не найден в наборе.")

    """Проверка, существует ли элемент в множестве."""
    def contains(self, element):
        return element in self.items

    """Проверка, существует ли элемент в множестве."""
    def intersection(self, other_set):
        result = Set()
        for item in self.items:
            if item in other_set.items:
                result.add(item)
        return result

    """Объединение текущего множества с другим."""
    def union(self, other_set):
        result = Set()
        for item in self.items:
            result.add(item)
        for item in other_set.items:
            result.add(item)
        return result

    """Разность текущего множества и другого."""
    def difference(self, other_set):
        result = Set()
        for item in self.items:
            if item not in other_set.items:
                result.add(item)
        return result

    """Строковое представление множества."""
    def __str__(self):
        return "{" + ", ".join(map(str, self.items)) + "}"

    """Возвращение размера множества."""
    def size(self):
        return len(self.items)

    """Проверка, пусто ли множество."""
    def is_empty(self):
        return len(self.items) == 0