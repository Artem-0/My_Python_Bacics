
def min_divider(number):
    for divider in range(2, number + 1):
        if number % divider == 0:
            return divider

user_number = int(input('Введите число: '))

print(f'Наименьший делитель, отличный от единицы: {min_divider(user_number)}')