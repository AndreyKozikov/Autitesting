## Урок 1. Тестирование cli в linux без использования фреймворков

Файлы с функциями расположены в папке [Seminar1](Seminar1)

### Задание 1.

Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна 
возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. 
Передаваться должна только одна строка, разбиение вывода использовать не нужно.

Решение: [task1.py](Seminar1/task1.py)

### Задание 2. (повышенной сложности)

Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка 
string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.

Решение: [task2.py](Seminar1/task2.py)