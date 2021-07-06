import codecs
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding="utf8") as file_obj:
    content = file_obj.read().splitlines()
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with codecs.open('file_5.txt', 'w', encoding="utf8") as file_obj_2:
    file_obj_2.writelines('\n'.join(new_file))
"""
Почему то гугл переводчик не работает... установил через пип инстал... даже пример интернета не работает ниже..
from googletrans import Translator

translator = Translator()
result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

print(result.src)
print(result.dest)
print(result.text)
"""