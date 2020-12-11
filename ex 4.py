my_list = [3, 5, 1, 2, 3, 6, 2, 1, 1, 91, 7, 9, 10, 5, 6, 7, 2, 3, 4, 12, 15]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
