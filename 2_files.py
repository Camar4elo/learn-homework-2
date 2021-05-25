"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='UTF-8') as file_1:
        line_counter = 0
        word_counter = 0
        for line in file_1:
            line = line.replace('\n', '')
            line_counter += len(line)
            word_counter += len(line.split())
            line = line.replace('.', '!')
            with open('referat2.txt', 'a', encoding='UTF-8') as file_2:
                file_2.write(f'{line}\n')
        print(line_counter)
        print(word_counter)

if __name__ == "__main__":
    main()
