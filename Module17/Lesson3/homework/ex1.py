#Задача 1. Список чётных чисел

left_border = int(input('Введите число A: '))
right_border = int(input('Введите число B: '))

even_list = [x for x in range(left_border, right_border + 1) if x % 2 == 0]

print(even_list)