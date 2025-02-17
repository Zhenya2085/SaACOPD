from LinkedListClass import LinkedList

# Создание нового связанного списка
linked_list = LinkedList()

# Добавление элементов в список
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Добавление элемента в начало списка
linked_list.prepend(5)

# Вывод списка
print("Список:", linked_list)  # Список: 5 -> 10 -> 20 -> 30

# Размер списка
print("Длина списка:", linked_list.size())  # Длина списка: 4

# Поиск элемента
node = linked_list.find(20)
if node:
    print(f"Найден узел с данными: {node.data}")  # Найден узел с данными: 20
else:
    print("Узел не найден!")

# Удаление элемента
linked_list.delete(20)
print("Список после удаления:", linked_list)  # Список после удаления: 5 -> 10 -> 30

# Удаление элемента, который не существует
linked_list.delete(40)
print("Список после попытки удалить несуществующий элемент:", linked_list)  # Список после попытки удалить несуществующий элемент: 5 -> 10 -> 30
