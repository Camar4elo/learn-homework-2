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
    with open('referat.txt', 'r', encoding='utf-8') as file_1:
        content = file_1.read()
        updated_content = content.replace('\n', '')
        print(len(updated_content))
        print(len(updated_content.split()))
        content = content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as file_2:
        file_2.write(f'{content}')
    

if __name__ == "__main__":
    main()
