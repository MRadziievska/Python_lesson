my_tuple_1 = (1, 2, 3)
# print(type(my_tuple_1), my_tuple_1)

my_tuple_2 = 1, 2, 3
# print(type(my_tuple_2), my_tuple_2)

my_tuple_3 = tuple([1, 2, 3])
# print(type(my_tuple_3), my_tuple_3)

# print(my_tuple_1[0])
# print(my_tuple_1[2])

#print(len(my_tuple_1)) # кол-во элкментов

# print(1 in my_tuple_1) # True (проверяем есть ли элемент)
# print(777 in my_tuple_1) # False (проверяем есть ли элемент)

#print(777 not in my_tuple_1) ## True (проверяем отсутствует ли элемент)

my_tuple_4 = 7,3,5
#print(my_tuple_1 + my_tuple_4) # (1, 2, 3, 7, 3, 5) можно склеевать кортежи
#print(my_tuple_4 +my_tuple_1) # (7, 3, 5, 1, 2, 3) от последовательности зависит от чего будет начинаться кортеж

# for i in my_tuple_1:
#     print(i)

# print(min(my_tuple_1))
# print(max(my_tuple_1))

# print(sum(my_tuple_1))

# print(my_tuple_1.index(2))

print(my_tuple_1.count(2))