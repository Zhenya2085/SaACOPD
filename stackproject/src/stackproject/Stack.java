/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package stackproject;

/**
 *
 * @author student
 */
import java.util.LinkedList;

public class Stack<T> {
    private LinkedList<T> items;

    // Конструктор
    public Stack() {
        items = new LinkedList<>();
    }

    // Добавление элемента на вершину стека (Push)
    public void push(T value) {
        items.addLast(value);
    }

    // Удаление элемента с вершины стека (Pop)
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return items.removeLast();
    }

    // Просмотр верхнего элемента без удаления (Peek)
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return items.getLast();
    }

    // Проверка на пустоту стека
    public boolean isEmpty() {
        return items.isEmpty();
    }

    // Получение количества элементов в стеке
    public int count() {
        return items.size();
    }

    // Для отображения стека (для отладки)
    public void displayStack() {
        for (int i = items.size() - 1; i >= 0; i--) {
            System.out.println(items.get(i));
        }
    }
}

