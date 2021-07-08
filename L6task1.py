import time
from itertools import cycle
import threading


class Thread(threading.Thread):
    pass


class TrafficLight:
    def __init__(self, __colors):
        self.__colors = __colors

    def run(self):
        for color, delay in cycle(self.__colors.items()):
            print(f'Загорелся {color}')
            time.sleep(delay)


t = TrafficLight({'Красный': 7, 'Желтый': 2, 'Зеленый': 5})
t.run()