/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package stackproject;

/**
 *
 * @author student
 */
import java.util.Scanner;

public class StackDemo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Создание экземпляра стека для хранения операндов
        Stack<Integer> values = new Stack<>();
        
        System.out.println("Введите выражение в обратной польской записи (например, '4 2 +'):");
        String input = scanner.nextLine();
        
        // Обработка ввода
        String[] tokens = input.split(" ");
        
        for (String token : tokens) {
            if (isInteger(token)) {
                // Если токен - это число, добавляем его в стек
                values.push(Integer.parseInt(token));
            } else {
                // Если токен - это оператор, выполняем операцию
                int rhs = values.pop();
                int lhs = values.pop();
                
                switch (token) {
                    case "+":
                        values.push(lhs + rhs);
                        break;
                    case "-":
                        values.push(lhs - rhs);
                        break;
                    case "*":
                        values.push(lhs * rhs);
                        break;
                    case "/":
                        values.push(lhs / rhs);
                        break;
                    default:
                        System.out.println("Неизвестная операция: " + token);
                        return;
                }
            }
        }

        // Вывод результата
        System.out.println("Результат: " + values.pop());
    }

    // Метод для проверки, является ли строка числом
    private static boolean isInteger(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}

