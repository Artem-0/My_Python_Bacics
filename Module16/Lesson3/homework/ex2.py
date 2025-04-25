first_str = input('Первое сообщение: ')
second_str = input('Второе сообщение: ')

first_count = first_str.count('!') + first_str.count('?')
second_count = second_str.count('!') + second_str.count('?')

if first_count > second_count:
    print(first_str + ' ' + second_str)
elif first_count < second_count:
    print(second_str + ' ' + first_str)
else:
    print('Ой')