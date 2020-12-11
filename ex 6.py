from itertools import cycle
from itertools import count


def count_func(start, stop):
    func_list = []
    for el in count(start):
        if el <= stop:
            func_list.append(el)
        else:
            return func_list


def cycle_func(func_list, counter):
    i = 0
    for el in cycle(func_list):
        if i <= counter:
            print(el)
            i += 1
        else:
            break


my_list = [123, 'qwerty', True, 13.5]
print(count_func(int(input('Укажите стартовое значение: ')), int(input('Укажите окончательное значение: '))))
cycle_func(my_list, int(input('Укажите количество циклов: ')))
