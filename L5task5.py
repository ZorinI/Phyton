import codecs
num = input('Введите числа через пробел: ')
with codecs.open('file_6.txt', 'w', 'utf-8') as my_f:
   my_num = num.split()
   print(f'Сумма чисел: {sum(map(int, my_num))}', file=my_f)