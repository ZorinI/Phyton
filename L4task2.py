my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_ = [el for num, el in zip(my_list, my_list[1:]) if el>num]
print(f'Исходный список {my_list}')
print(f'Новый список {new_}')