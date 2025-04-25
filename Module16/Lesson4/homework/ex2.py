members = []

n = int(input('Кол-во участников: '))
k = int(input('Кол-во человек в команде: '))

if n % k == 0:
    num = 1
    for _ in range(n // k):
        members.append(list(range(num, num + k)))
        num += k
    print('Общий список команд:', members)
else:
    print(f'{n} участников невозможно поделить на команды по {k} человек!')