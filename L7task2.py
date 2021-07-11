from abc import ABC, abstractmethod


class shmot(ABC):
    def __init__(self, param):
        self.param = param
 """чет поплыл тут, через __add_ хотел не получилось..и чет не получается вывести общую площадь"""
"""def __add__(self, other):
    return f'Объединение двух клеток: {self.zxc + other.zxc}'"""

    def ploshad(self):
        return f'Площадь затраченной ткани: {(self.param / 6.5 + 0.5) + (2 * self.param + 0.3)}'


    @abstractmethod
    def abstractmethod(self):
        pass


class kostum(shmot):
    def __init__(self, param):
        super(kostum, self).__init__(param)

    def ploshad(self):
        return f'Ткани для пошива костюма: {self.param / 6.5 + 0.5:.2f}'

    def abstractmethod(self):
        pass


class palto(shmot):
    def __init__(self, param):
        super(palto, self).__init__(param)

    def ploshad(self):
        return f'Ткани для пошива пальто: {2 * self.param + 0.3:.2f}'

    def abstractmethod(self):
        pass


kostum = kostum(8)
palto = palto(7)


print(kostum.ploshad())
print(palto.ploshad())