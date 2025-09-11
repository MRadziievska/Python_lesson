# sequence_1 = range(5)
# print(sequence_1, type(sequence_1))
#
# for i in sequence_1:   # 0 1 2 3 4 (показывает, что включает в себя)
#     print(i)
# new_list = list(range(5)) # [0, 1, 2, 3, 4] <class 'list'> (превращает в список)
# print(new_list, type(new_list))

# for i in range(7, 10): # 7 8 9 (так как 10 не включается) - два аргумента
#     print(i)

# for i in range(0, 11, 2):  # три аргумента - 0 2 4 6 8 10 (числа от 0 до 11 (не включая) с шагом (2) через 1
#     print(i)

# for i in range(5):
#     print(i)
# for j in range(10, 15):  # без отступа: 012341011121314
#     print(j)

# for i in range(5):
#     print(i)
#     for j in range(10, 15): # с отступом: 0 10 11 12 13 14 1 10 11 12 13 14 2 10 11 12 13 14 3 10 11 12 13 14 4 10 11 12 13 14
#         print(j)

# Таблица умножения:

for i in range(2, 10):
    print(f"=={i}==")
    for j in range(2, 10):
        print(f"{i}*{j}={i*j}")


# ==2==
# 2*2=4
# 2*3=6
# 2*4=8
# 2*5=10
# 2*6=12
# 2*7=14
# 2*8=16
# 2*9=18

# ==3==
# 3*2=6
# 3*3=9
# 3*4=12
# 3*5=15
# 3*6=18
# 3*7=21
# 3*8=24
# 3*9=27

...