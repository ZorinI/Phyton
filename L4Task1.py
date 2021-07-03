from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    resuslt = time * salary + bonus
    print('Отработано в часах: ', time)
    print('Ставка в час: ', salary)
    print('Премия: ', bonus)
    print(f'заработная плата сотрудника  {resuslt}')
except ValueError:
    print("введите числа!")