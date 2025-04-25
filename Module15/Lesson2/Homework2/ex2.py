# Задача 2. Кратность
# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран
# сумму индексов элементов списка, которые кратны K.

num_list = []

num_count = int(input('Кол-во чисел в списке: '))

for number in range(num_count):
    print('Введите', number + 1, 'число: ', end = ' ')
    num = int(input())
    num_list.append(num)

# print(num_list)
divider = int(input('Введите делитель: '))
summ = 0

for number in range(num_count):
    if num_list[number] % divider == 0:
        print('Индекс числа', num_list[number], ':', number)
        summ += number

print('Сумма индексов:', summ)