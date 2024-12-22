import random
import inspect


def introspection_info(obj):
    print(f'{obj}:')
    dict = {}
    dict['Тип объекта'] = type(obj).__name__
    dict['Атрибуты объекта'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    dict['Методы объекта'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    dict['Модуль, к которому объект принадлежит'] = inspect.getmodule(obj)
    return dict


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word = random.choice(self.words)
        return word


number_info = introspection_info(42)
print(number_info)
print()

first_ball = MysticBall('Да', 'Нет', 'Наверное')
class_info = introspection_info(first_ball)
print(class_info)
