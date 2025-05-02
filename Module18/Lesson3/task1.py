# Задача "Путь к файлу"

user_name = input('Введите имя пользователя: ')
file_name = input('Введите имя файла: ')

path = 'D:/{user}/docs/folder/{new_file}'.format(
    user = user_name,
    new_file = file_name
)

# if path[-4:] == '.txt':
#     print('Путь к файлу:', path)
# else:
#     print('Ошибка! Неверное расширение файла.')

if not path.endswith('.txt'):
    print('Ошибка! Неверное расширение файла.')
elif not path.startswith('C:/'):
    print('Ошибка! Неверно указан диск.')
else:
    print('Путь к файлу:', path)