# TODO здесь писать код
def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10

    return sum

def count_of_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10

    return count

user_number = int(input('Введите число: '))

print(f'\nСумма чисел: {sum_of_digits(user_number)}')
print(f'Количество цифр в числе: {count_of_digits(user_number)}')
print(f'Разность суммы и количества цифр: {sum_of_digits(user_number) - count_of_digits(user_number)}')