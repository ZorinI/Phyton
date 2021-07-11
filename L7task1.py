class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for i in range(len(other.my_list[el])):
                self.my_list[el][i] = self.my_list[el][i] + other.my_list[el][i]
        return Matrix.__str__(self)


matrix_1 = Matrix([[1, 2, 3], [4, 140, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1 + matrix_2)