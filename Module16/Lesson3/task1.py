# Задача "Любимые фильмы"

my_list = ['Игра', 'Изгой', 'Таксист']
your_list = ['Начало', 'Отступники', 'Король Лев']

# for i_elem in your_list:
#     my_list.append(i_elem)

#my_list.extend(your_list)

# my_list += your_list - ОЧЕНЬ МЕДЛЕННО!

my_list.extend('Алладин')

# my_list.extend(123) - ОШИБКА!
for i_elem in my_list:
    print(i_elem)