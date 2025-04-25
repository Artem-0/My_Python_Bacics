# Задача "Замена символа"

word = input('Введите слово: ')
replase_num = int(input('Номер символа для замены: '))
replase_sym = input('Чем заменяем: ')

sym_list = list(word)

sym_list[replase_num - 1] = replase_sym

for i in sym_list:
    print(i, end = '')