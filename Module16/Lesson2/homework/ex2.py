# Задача 2. Сокращения

count_employees = int(input('Кол-во сотрудников: '))
list_salary = []

for i_emp in range(count_employees):
    salary = int(input(f'Зарплата {i_emp + 1} сотрудника: '))
    if salary != 0:
        list_salary.append(salary)

print('\nОсталось сотрудников:', len(list_salary))
print('Зарплаты:', list_salary)

print('\nМаксимальная зп:', max(list_salary))
print('Минимальная зп:', min(list_salary))