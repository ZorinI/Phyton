#задача 1

my_list = [False, bool, None, "asdfasdf", True, 5, 5.5]
def my_type(list):
    for list in range(len(my_list)):
        print(type(my_list[list]))
    return
my_type(my_list)

#задача 2

count = int(input("введи кол-во элм. списка: "))
my_list = []
i = 0
n= 0
while i < count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
for element in range(int(len(my_list)/2)):
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n += 2
print(my_list)

#Задача 3

My_list = ["зима", "весна", "лето", "осень"]
seasons_dict = {1 : "весна", 2 : "лето", 3 : "осень", 4 : "зима"}
month = int(input("Введите номер месяца: "))
if range (1, 12, 2):
        print(seasons_dict.get(4))
        print(My_list[0])
elif range (3, 4, 5):
    print(seasons_dict.get(1))
    print(My_list[1])
elif range (6, 7, 8):
    print(seasons_dict.get(2))
    print(My_list[2])

elif range (9, 10, 11):
    print(seasons_dict.get(4))
    print(My_list[3])
else:
    print("Такого месяца не существует")


#Задача 4
my_str = input("Введите несколько слов в строку:  ")
my_word = []
numb = 1
for n in range(my_str.count(" ") + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {numb} {my_word [n]}")
        numb += 1
    else:
        print(f" {numb} {my_word [n] [0:10]}")
        numb += 1


#задача 5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
n = int(input("Введите число: для выхода наберите - 000) "))
while n != 000:
    for m in range(len(my_list)):
        if my_list[m] == n:
            my_list.insert(m + 1, n)
            break
        elif my_list[0] < n:
            my_list.insert(0, n)
        elif my_list[-1] > n:
            my_list.append(n)
        elif my_list[m] > n and my_list[m + 1] < n:
            my_list.insert(m + 1, n)
    print(f"текущий список - {my_list}")
    n = int(input("Введите число "))