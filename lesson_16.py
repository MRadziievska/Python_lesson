our_dict = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3", "key_9": [1, 2, 3]}
# # print(our_dict["key_1"])
#
# print(our_dict.get("key_1"))
# print(our_dict.get("key_4")) # (dict.get()), позволяет получить значение по ключу,
# # при этом возвращая значение по умолчанию (или None), если ключ отсутствует, и не вызывая ошибку KeyError
#
# print("last_line")
#
# print(our_dict.setdefault("key_5", "value_5")) # eсли ключ существует, метод .setdefault возвращает его значение;
# # если ключ отсутствует, он добавляет его в словарь с указанным значением (или None)
# print(our_dict.setdefault("key_1", "value_6"))
# print(our_dict)
#
# our_dict["key_1"] = "value_6" # add or change
# our_dict["key_6"] = "value_6"
# #or
# our_dict.update({"key_1": "value_7"})
# our_dict.update({"key_8": "value_8"})
#
# del our_dict["key_8"] # del- для удаления объектов: переменные, элементы списков, словарей, срезов (частей) и даже атрибуты объектов
# # если объект отсутвует, выдает ощибку
# print(our_dict.pop("key_9", "key not exist")) # pop() удаляет элемент из словаря по указанному ключу и возвращает его значение
# print(our_dict)
#
# our_dict.popitem()  # удаляет последнюю добавленную пару ключ-значение
# print(our_dict)
#
# our_dict.clear()  # полностью очищает словарь
# print("->", our_dict)

# our_dict_2 = our_dict.copy()  # копирует
# our_dict_2.update({"key_10": "value_10"})
# our_dict_2["key_9"].append("11") # изменяет 2 словаря (так как копия привязана к изночальному списку
#
# print(our_dict)
# print(our_dict_2)

# from copy import deepcopy
#
# our_dict_2 = deepcopy(our_dict)  # копирует
# our_dict_2.update({"key_10": "value_10"})
# our_dict_2["key_9"].append("11") # изменяет только 2-ой словарь
#
# print(our_dict)
# print(our_dict_2)

# for i in our_dict.keys(): # чтоб пройтись по ключам
#     print(i)

# for i in our_dict.values(): # чтоб пройтись по значениям
#     print(i)

for key, value in our_dict.items(): ## чтоб пройтись и по ключам, и по значениям
    print(key)
    print(value)

