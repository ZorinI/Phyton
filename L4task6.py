from itertools import count, cycle
for el_1 in count(3):
    if el_1 == 10:
        break
    else:
        print(el_1)

print()

x = 0
for el_2 in cycle('ABC'):
    if x == 10:
        break
    else:
        print(el_2)
    x += 1