# print(dir([1, 2, 3]))

l_1 = [1, 2, 3, 1, 777]
l_2 = [1, 777, 999]

# l_1.append(555) # [1, 2, 3, 1, 777, 555] добавить в список 555
# print(l_1)
#
# l_1.append(l_2) # [1, 2, 3, 1, 777, 555, [1, 777, 999]] добавить в список другой список
# print(l_1)

# l_1.extend(l_2) # [1, 2, 3, 1, 777, 1, 777, 999] распаковывает все списки в один без доп. скобок
# print(l_1)
#
# l_1.insert(1, 34) # [1, 34, 2, 3, 1, 777, 1, 777, 999] указывает место куда вставить объект (34)
# print(l_1)

# print(l_1.count(1)) # 2 - количество 1
#
# print(l_1.index(3)) #2
# print(l_1.index(1)) #0

# l_1.reverse() # [777, 1, 3, 2, 1] обратный список
# print(l_1)
#
# l_1.pop() # удаляет последний элемент
# print(l_1)

# l_1.pop(2) # удаляет указанный эл.
# print(l_1)

# del_element = l_1.pop(2) # сохраняет удалённый эл.
# print(l_1)
# print(del_element)

# new_list = l_1.copy() #  сохранения и смены id (работает с одномерными списками)
# print(id(new_list)) # 2237374333760
# print(id(l_1)) # 2237373850304

# new_list = l_1[::] # для сохранения и смены id (работает с одномерными списками)
# print(id(new_list)) # 2237374333760
# print(id(l_1))

# print(l_1) # [1, 2, 3, 1, 777]
# l_1.sort()
# print(l_1) # [1, 1, 2, 3, 777]

# l_4 = ["apple", "tea", "lemon", "python"]
# l_4.sort(key=len) # ['tea', 'apple', 'lemon', 'python'] по кол-ву букв в слове
# print(l_4)

# l_4 = ["apple", "tea", "lemon", "python"]
# l_4.sort(key=len, reverse=True) # ['python', 'apple', 'lemon', 'tea'] от длинного слова к короткому
# print(l_4)

l_1.clear() # [] для очистки списка
print(l_1)







