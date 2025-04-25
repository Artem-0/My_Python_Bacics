# Задача 3. IP-адрес
num_list = []

while True:
    number = int(input('Введите число: '))
    if 0 < number <= 255:
        num_list.append(number)
    else:
        print('Число вне диапазона от 0 до 255!')
    if len(num_list) == 4:
        break

ip_address = '{0}.{1}.{2}.{3}'.format(num_list[0], num_list[1], num_list[2], num_list[3])
print('IP-адрес:', ip_address)