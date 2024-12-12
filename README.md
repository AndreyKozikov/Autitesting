## Урок 4. Реализации автодеплоя и тестов по SSH

Данное задание является промежуточной аттестацией.

Файлы с функциями расположены в папке [Seminar4](Seminar4)

Результаты тестирования отражены в отчете: [report.html](Seminar4/report.html)

### Задание 1.

Условие:
Переделать все шаги позитивных тестов на выполнение по SSH. Проверить работу.

Решение: [test_7z.py](Seminar4/test_7z.py)

### Задание 2. (дополнительное задание)

Условие:

Переделать все шаги негативных тестов на выполнение по SSH. Проверить работу.

Решение: [test_7z_negative.py](Seminar4/test_7z_negative.py)

---

## Урок 3. Использование фикстур в pytest. Создание отчетов о тестировании

Файлы с функциями расположены в папке [Seminar3](Seminar3)

Результаты тестирования отражены в отчете: [report.html](Seminar3/report.html)

### Задание 1.

Условие:
Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

Решение: [fixtures.py](Seminar3/fixtures.py)

Задание 2. (дополнительное задание)

Дополнить все тесты ключом команды 7z -t (тип архива). Вынести этот параметр в конфиг.

Решение: [test_7z.py](Seminar3/test_7z.py)

---

## Урок 2. Создание первых тестов на pytest

Файлы с функциями расположены в папке [Seminar2](Seminar2)

### Задание 1.

Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

### Задание 2.

• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

Решение обеих задач: [test_7z.py](Seminar2/test_7z.py)

---

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