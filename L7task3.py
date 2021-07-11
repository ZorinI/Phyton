class Cell:
    def __init__(self, zxc):
        self.zxc = int(zxc)

    def __add__(self, other):
        return f'Объединение двух клеток: {self.zxc + other.zxc}'

    def __sub__(self, other):
        try:
            if self.zxc - other.zxc <= 0:
                raise ValueError
            else:
                return f'Клетка стала меньше: {self.zxc - other.zxc}'
        except ValueError:
            print('Операция не возможна')

    def __mul__(self, other):
        return f'Создаётся общая клетка: {self.zxc * other.zxc}'

    def __truediv__(self, other):
        return f'Создаётся клетка из деления: {self.zxc // other.zxc}'

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.zxc // row)]
        ordered.append('*' * (self.zxc % row))
        return f'\n'.join(ordered)


cell_1 = Cell(5)
cell_2 = Cell(2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print()
print(cell_2.make_order(5))