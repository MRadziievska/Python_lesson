# my_dict = {"first_key": "first_value", 777: [34,1000], (45, 1): 4324}
# print(my_dict["first_key"])
# print(my_dict[777])
# print(my_dict[(45, 1)])

# dict_1 = {"first_key": "first_value", "second_key": "second_value"}
# print(type(dict_1))
# print(dict_1)

# dict_2 = dict([["first_key", "first_value"], ["second_key", "second_value"]])
# print(type(dict_2))
# print(dict_2)         # <class 'dict'> {'first_key': 'first_value', 'second_key': 'second_value'}

dict_3 = dict.fromkeys(["key_1", "key_2", "key_3"], "value")
print(type(dict_3))
print(dict_3)        # <class 'dict'>  {'key_1': 'value', 'key_2': 'value', 'key_3': 'value'}
