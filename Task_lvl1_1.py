# # Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len('a'))


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
count = 0
my_list = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
for letter in word:
    if letter in my_list:
        count += 1
print(count)
    

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'.split()
for word in sentence:
    print(word[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'.split()
average_len = 0
count = 0
for word in sentence:
    count += 1
    average_len += len(word)
print(average_len / count)