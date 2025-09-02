
our_string = "Hello world" # h-0 e-1 l-2 l-3 o-4 пробел-5 w-6 o-7 r-8 d-9

# print(our_string.upper()) # HELLO WORLD
# print(our_string.lower()) # hello word
# print(our_string.count("l")) # 3 (сколько раз встречается символ)
# print(our_string.count("ll")) # 1 (сколько раз встречается символ)
# print(our_string.count("l", 3)) # 2 (что искать, и с какого эл. начинать)
# print(our_string.count("l", 3, 7)) # 1 (что искать, с какого эл. начинать и каким закончить)
# print(our_string.find("wor")) # 6
# print(our_string.find("o")) # 4
# print(our_string.rfind("o")) # 7
# print(our_string.find("apple")) # -1 (если символов нет, то возвращает -1)
# print(our_string.index("apple")) # ValueError: substring not found (если символов нет, то возвращает ошибку)
# print(our_string.replace("Hello", "Hi")) # Hi world
# print(our_string.replace(" ", " ")) #Helloworld (уберет пробелы)
# print(our_string.isalpha()) # False (если пробел или спец символ)
# print("fjlnmk".isalpha()) # True (если буквы)
# print("789".isdigit()) # True (если целое, положительное)
# print("text".rjust(10)) # ______text (пространство будет заполняться пробелами слева)
# print("text".rjust(10, "!")) # !!!!!!text
# print("text".ljust(10, "1")) # text111111 (справа)

new_string = "      hi      "
# print(new_string.strip()) # hi (удаляет пробелы)
# print(new_string.lstrip()) # hi (слева)
# print(new_string.rstrip()) #       hi (справа)



