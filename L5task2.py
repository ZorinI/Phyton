with open('file_2.txt', 'r', encoding="utf8") as my_f:
    content = my_f.readlines()
    print(f'Количество строк: {len(content)}')
    for i in range(len(content)):
        print(f'Количество слов в: {i + 1} строке - {len(content[i].split())}')