from SetClass import Set

# Создание множеств
set1 = Set()
set2 = Set()

# Добавление элементов в множества
set1.add(1)
set1.add(2)
set1.add(3)

set2.add(3)
set2.add(4)
set2.add(5)

# Вывод множества
print("Множество 1:", set1)  # Set 1: {1, 2, 3}
print("Множество 2:", set2)  # Set 2: {3, 4, 5}

# Пересечение множеств
intersection_set = set1.intersection(set2)
print("Пересечение:", intersection_set)  # Пересечение: {3}

# Объединение множеств
union_set = set1.union(set2)
print("Объединение:", union_set)  # Объединение: {1, 2, 3, 4, 5}

# Разность множеств
difference_set = set1.difference(set2)
print("Разность (мн-во1 - мн-во2):", difference_set)  # Разность (мн-во1 - мн-во2): {1, 2}

# Проверка наличия элемента
print("Множество 1 содержит 2:", set1.contains(2))  # Множество 1 содержит 2: True
print("Множество 1 содержит 4:", set1.contains(4))  # Множество 1 содержит 4: False

# Удаление элемента
set1.remove(2)
print("Множество 1 после удаления 2:", set1)  # Множество 1 после удаления 2: {1, 3}

# Размер множества
print("Размер множества 1:", set1.size())  # Размер множества 1: 2

# Проверка, пусто ли множество
print("Набор 1 пуст?", set1.is_empty())  # Набор 1 пуст? False
