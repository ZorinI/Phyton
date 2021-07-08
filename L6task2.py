class Road:
    def __init__(self, _length, _width, _mass, _tolsh):
        self._length = _length
        self._width = _width
        self._mass = _mass
        self._tolsh = _tolsh

    def mass_sum(self):
        return self._mass * self._tolsh * self._length * self._width / 1000


r = Road(20, 5000, 25, 5)
print(f'Масса покрытия: {r.mass_sum()} Тонн.')
