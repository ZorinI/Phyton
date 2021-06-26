def print_user_data(name, surname, year, city, email, phone):
     user = {'имя': name,'фамилия': surname,'год рождения': year, 'город': city, 'email': email, 'тел': phone}
     return user

print(print_user_data(name = input('имя'), surname = input('фамилия'), year = int(input('гож рождения')), city = input('город'), email = input('email'), phone = input('тел')))


