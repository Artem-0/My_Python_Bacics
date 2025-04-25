employees = int(input('Кол-во сотрудников в офисе: '))
list_employee_id = []

for _ in range(employees):
    employee_id = int(input('ID сотрудника: '))
    list_employee_id.append(employee_id)

id_to_find = int(input('Какой ID ищем? '))

if id_to_find not in list_employee_id:
    print('Сотрудник не работает!')
else:
    print('Сотрудник на месте')