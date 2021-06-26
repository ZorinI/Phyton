def my_sum():
    sum_res = 0
    exit = False
    while exit == False:
        """ввод чисел """
        number = input('Введите числа через пролем или Q для выхода: ').split()
        """ показывает все числа"""
        print(number)
        res = 0
        for element in range(len(number)):
            """проверяем не содержит ли выход"""
            if number[element] == 'q' or number[element] == 'Q':
                exit = True
                break
            else:
                """суммируем числа"""
                res = res + int(number[element])
        sum_res = sum_res + res
        print(f'Текущаяя сумма {sum_res}')
    print(f'конечная сумма {sum_res}')

my_sum()