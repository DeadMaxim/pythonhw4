my_list = [10, 13, 1, 21, 5, 11, 35, 246, 79, 45, 67, 100]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)