from functools import reduce


def my_func(prev_el, next_el):
    return prev_el * next_el


my_list = [el for el in range(100, 1001, 2)]
print(reduce(my_func, my_list))
another_list = [el for el in range(100, 1001) if el % 2 == 0]
print(another_list)
