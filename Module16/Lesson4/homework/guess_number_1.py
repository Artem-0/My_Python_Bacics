print('Игра Угадай число! \nЗагадай число\nА я отгадаю')
min = 1
max = 100
ansver = max // 2
print('N =', ansver)
count = 1
while True:
  i = int(input('Твоё число равно, больше или меньше N? 1 — равно, 2 — больше, 3 — меньше '))
  if i == 1:
    print('Я угадал число с', count, 'попытки!')
    break
  elif i == 2:
    min = ansver + 1 # 51 # 76 # 89 # 95 # 98 # 100            # 26
    ansver = (min + max) // 2 # 75 # 88 # 94 # 97 # 99 # 100   # 37
    print('N =', ansver)
  else:
    max = ansver - 1 # 49 # 24 # 11 # 5 # 2
    ansver = (min + max) // 2 # 25 # 12 # 6 # 3 # 1
    print('N =', ansver)
  count += 1