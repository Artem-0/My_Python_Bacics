# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется на следующую
# по алфавиту через K позиций по кругу.
#
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
# Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.

def caesar_cipher(text, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' '
                  else ' ') for sym in text]
    encrypted_text = ''.join(char_list)
    return encrypted_text

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

encrypted_text = caesar_cipher(text, shift)

print('Зашифрованное сообщение:', encrypted_text)