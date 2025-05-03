#Задача "Подсчёт слов"

words_list = []

for i_num in range(3):
    print('Введите', i_num + 1, 'слово:', end = ' ')
    # word = input().lower()
    word = input().upper()
    words_list.append(word)

# text = input('Введите текст: ').lower().split()
text = input('Введите текст: ').upper().split()

print('\nПодсчёт слов в тексте ')
for index in range(3):
    print(words_list[index], ':', text.count(words_list[index]))