#Задача 2. Сообщение

string = input('Введите строку: ')
character = input('Введите дополнительный символ: ')

fir_list = [char + char for char in string]
sec_list = [char + character for char in fir_list]

print('Список удвоенных символов:', fir_list)
print('Склейка с дополнительным символом:', sec_list)