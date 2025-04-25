import random

print('Игра Угадай число! \nЗагадай число\nА я отгадаю')
list = list(range(1, 101))
print(list)
ansver = random.choice(list)
print('N =', ansver)
count = 1
while True:
  i = int(input('Твоё число равно, больше или меньше N? 1 — равно, 2 — больше, 3 — меньше: '))
  if i == 1:
    print('Я угадал число с', count, 'попытки!')
    break
  elif i == 2:
    start = 0
    stop = list.index(ansver) + 1
    del list[start : stop]
    print(list)
    ansver = random.choice(list)
    print('N =', ansver)
  else:
    start = list.index(ansver)
    stop = len(list)
    del list[start : stop]
    print(list)
    ansver = random.choice(list)
    print('N =', ansver)
  count += 1