# Дана строка S и номер позиции символа в строке. Напишите программу,
# которая выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей:
# их нет, есть ровно один или есть два таких же.

s = input('Введите строку: ')
list_s = list(s)

sym_number = int(input('Номер символа: ')) - 1

print('Символ слева:', list_s[sym_number - 1])
print('Символ справа:', list_s[sym_number + 1])

if list_s[sym_number - 1] == list_s[sym_number + 1] or list_s[sym_number] == list_s[sym_number - 1] or list_s[sym_number] == list_s[sym_number + 1]:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')